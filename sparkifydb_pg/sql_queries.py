# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES
songplay_table_create = """create table if not exists songplays 
(
    songplay_id serial, 
    user_id integer, 
    song_id text, 
    artist_id text, 
    session_id integer,
    start_time integer,
    level text,  
    location text, 
    user_agent text,
    unique(user_id),
    unique(song_id),
    unique(artist_id),
    unique(user_id, session_id),
    constraint songplays_pkey primary key (songplay_id)
    
);
"""

user_table_create = """create table if not exists users
(
    user_id integer, 
    first_name text, 
    last_name text, 
    gender varchar(1), 
    level text,
    constraint users_pkey primary key (user_id)
);
"""

song_table_create = """create table if not exists songs
(
    song_id text,
    artist_id text,
    title text,
    year smallint,
    duration integer,
    constraint songs_pkey primary key (song_id)
);
"""

artist_table_create = """create table if not exists artists
(
    artist_id text, 
    name text, 
    location text, 
    latitude integer, 
    longitude integer,
    constraint artists_pkey primary key (artist_id)
);
"""

time_table_create = """create table if not exists time
(
    start_time integer, 
    hour smallint, 
    day smallint, 
    week smallint, 
    month smallint, 
    year smallint, 
    weekday smallint,
    constraint time_pkey primary key (start_time)
);
"""

# INSERT RECORDS

songplay_table_insert = """insert into songplays 
(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values %s
"""

user_table_insert = """insert into users
(user_id, first_name, last_name, gender, level) values %s
"""

song_table_insert = """insert into songs
(song_id, title, artist_id, year, duration) values %s 
on conflict on constraint songs_pkey do nothing
"""

artist_table_insert = """insert into artists
(artist_id, name, location, latitude, longitude) values %s
"""

time_table_insert = """insert into time
(start_time, hour, day, week, month, year, weekday) values %s
"""

# FIND SONGS

song_select = """
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
