import json
import psycopg2
from psycopg2.extras import execute_values, execute_batch
from sql_queries import *
from dotenv import dotenv_values
from pathlib import Path
from datetime import datetime


def process_song_file(cur, all_files):
    """
    - Process song files
    - Retrieve relevant files for songs and artists tables
    """

    song_data = []
    artist_data = []

    for f in all_files:
        with open(f, "r") as fhand:
            record = json.load(fhand)
            song_data.append(
                (
                    record["song_id"],
                    record["title"],
                    record["artist_id"],
                    record["year"],
                    record["duration"],
                )
            )
            artist_data.append(
                (
                    record["artist_id"],
                    record["artist_name"],
                    record["artist_location"],
                    record["artist_latitude"],
                    record["artist_longitude"],
                )
            )

    # insert song and artist data
    execute_values(cur, song_table_insert, song_data)
    execute_values(cur, artist_table_insert, artist_data)


def process_log_file(cur, all_files):
    """
    - Process all log files
    - Retrieve relevant fields for users, time and song plays tables
    """

    user_data = []
    time_data = []
    song_plays_data = []

    for f in all_files:
        with open(f, "r") as fhand:
            for line in fhand:
                record = json.loads(line.rstrip("\n"))

                if record["page"] != "NextSong":
                    continue

                # users
                user_data.append(
                    (
                        record["userId"],
                        record["firstName"],
                        record["lastName"],
                        record["gender"],
                        record["level"],
                    )
                )

                # time
                t = datetime.fromtimestamp(record["ts"] / 1000)
                time_data.append(
                    (
                        record["ts"],
                        t.hour,
                        t.day,
                        t.isocalendar()[1],
                        t.month,
                        t.isocalendar()[0],
                        t.isocalendar()[2],
                    )
                )

                # songplays
                cur.execute(
                    song_select,
                    (record["song"], record["artist"], round(record["length"])),
                )

                results = cur.fetchone()
                if results:
                    songid, artistid = results
                else:
                    songid, artistid = None, None

                song_plays_data.append(
                    (
                        record["userId"],
                        songid,
                        artistid,
                        record["sessionId"],
                        record["ts"],
                        record["level"],
                        record["location"],
                        record["userAgent"],
                    )
                )
    # insert users, time and song plays data into database
    execute_batch(cur, user_table_insert, user_data)  # execute_values does not work
    execute_values(cur, time_table_insert, time_data)
    execute_values(cur, songplay_table_insert, song_plays_data)


def process_data(cur, conn, filepath, func):
    """
    Get files in filepath and call relevant function for
    processing the files
    """

    # get all files matching extension from directory
    all_files = list(filepath.rglob("*.json"))

    # get total number of files found
    num_files = len(all_files)
    print("{} files found in {}".format(num_files, filepath))

    func(cur, all_files)
    conn.commit()


def main():
    """
    connect to database and obtain cursor
    call function to process songs and log data files
    """

    config = dotenv_values(".env")
    param_string = f"host={config['HOST']} dbname=sparkifydb user={config['USER']} password={config['PASSWORD']}"
    conn = psycopg2.connect(param_string)
    cur = conn.cursor()

    process_data(
        cur, conn, filepath=Path.cwd() / "data" / "song_data", func=process_song_file
    )
    process_data(
        cur, conn, filepath=Path.cwd() / "data" / "log_data", func=process_log_file
    )

    conn.close()


if __name__ == "__main__":
    main()
