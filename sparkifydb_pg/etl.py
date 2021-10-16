import os
import glob
import psycopg2
from psycopg2.extras import execute_values
import json
from sql_queries import *
from dotenv import dotenv_values
from pathlib import Path


def process_song_file(cur, all_files):

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


def process_log_file(cur, filepath):
    pass
    # open log file
    # df =

    # # filter by NextSong action
    # df =

    # # convert timestamp column to datetime
    # t =

    # # insert time data records
    # time_data =
    # column_labels =
    # time_df =

    # for i, row in time_df.iterrows():
    #     cur.execute(time_table_insert, list(row))

    # # load user table
    # user_df =

    # # insert user records
    # for i, row in user_df.iterrows():
    #     cur.execute(user_table_insert, row)

    # # insert songplay records
    # for index, row in df.iterrows():

    #     # get songid and artistid from song and artist tables
    #     cur.execute(song_select, (row.song, row.artist, row.length))
    #     results = cur.fetchone()

    #     if results:
    #         songid, artistid = results
    #     else:
    #         songid, artistid = None, None

    #     # insert songplay record
    #     songplay_data =
    #     cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = list(filepath.rglob("*.json"))

    # get total number of files found
    num_files = len(all_files)
    print("{} files found in {}".format(num_files, filepath))

    func(cur, all_files)
    conn.commit()


def main():
    config = dotenv_values(".env")
    param_string = f"host={config['HOST']} dbname=sparkifydb user={config['USER']} password={config['PASSWORD']}"
    conn = psycopg2.connect(param_string)
    cur = conn.cursor()

    process_data(
        cur, conn, filepath=Path.cwd() / "data" / "song_data", func=process_song_file
    )
    # process_data(cur, conn, filepath="data/log_data", func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
