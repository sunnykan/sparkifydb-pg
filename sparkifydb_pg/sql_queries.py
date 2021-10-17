# Drop tables

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# Create tables
songplay_table_create = """create table if not exists songplays 
(
    songplay_id serial, 
    user_id integer not null, 
    song_id text, 
    artist_id text, 
    session_id integer,
    start_time bigint not null,
    level text,  
    location text, 
    user_agent text,
    constraint songplays_pkey 
        primary key (songplay_id),
    constraint fk_user
        foreign key(user_id)
            references users(user_id),
    constraint fk_song
        foreign key(song_id)
            references songs(song_id),
    constraint fk_artist
        foreign key(artist_id)
            references artists(artist_id),
    constraint fk_start_time
        foreign key(start_time)
            references time(start_time)    
);
"""

user_table_create = """create table if not exists users
(
    user_id integer not null, 
    first_name text, 
    last_name text, 
    gender varchar(1), 
    level text,
    constraint users_pkey primary key (user_id)
);
"""

song_table_create = """create table if not exists songs
(
    song_id text not null,
    artist_id text not null,
    title text,
    year smallint,
    duration integer,
    constraint songs_pkey primary key (song_id)
);
"""

artist_table_create = """create table if not exists artists
(
    artist_id text not null, 
    name text, 
    location text, 
    latitude integer, 
    longitude integer,
    constraint artists_pkey primary key (artist_id)
);
"""

time_table_create = """create table if not exists time
(
    start_time bigint not null, 
    hour smallint, 
    day smallint, 
    week smallint, 
    month smallint, 
    year smallint, 
    weekday smallint,
    constraint time_pkey primary key (start_time)
);
"""

# Queries for inserting records

songplay_table_insert = """insert into songplays 
(user_id, song_id, artist_id, session_id, start_time, level, location, user_agent) values %s
"""

user_table_insert = """insert into users
(user_id, first_name, last_name, gender, level) values (%s,  %s,  %s,  %s,  %s)
on conflict on constraint users_pkey
    do update set level = EXCLUDED.level
"""

song_table_insert = """insert into songs
(song_id, title, artist_id, year, duration) values %s 
on conflict on constraint songs_pkey 
    do nothing
"""

artist_table_insert = """insert into artists
(artist_id, name, location, latitude, longitude) values %s
on conflict on constraint artists_pkey 
    do nothing
"""

time_table_insert = """insert into time
(start_time, hour, day, week, month, year, weekday) values %s
on conflict on constraint time_pkey 
    do nothing
"""

# Retrieve song ids and artist ids

song_select = """select s.song_id, a.artist_id 
from songs s 
join artists a 
on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s;
"""

# Query lists

create_table_queries = [
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
    songplay_table_drop,
]
