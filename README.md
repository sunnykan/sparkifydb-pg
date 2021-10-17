# Project Summary

Analyze data on songs and user activity on a music streaming app to understand what music users are listening to on the service. Design a database schema to facilitate the analysis. User activity and metadata on songs are recorded in separate JSON files which are kept in separate directories. Create an ETL pipeline to populate the new Postgres database using data from these files in the two directories. The database uses a star schema with a fact table and several dimension tables.

# Schema

![ER Diagram](https://github.com/sunnykan/sparkifydb_pg/blob/main/images/er_diagram.png "ER Diagram")

* Ideally, to comply with a star schema, **artist_id** should be dropped from the songs table.

# Execution
Clone the project and run the following commands in order:

1. To connect to the database and create the tables, run `python sparkifydb_pg/create_tables.py`
2. To populate the tables, run `python sparkifydb_pg/etl.py`
3. Query the database

# Files

[sql_queries.py](https://github.com/sunnykan/sparkifydb_pg/blob/main/sparkifydb_pg/sql_queries.py): Contains all relevant queries that are used for creating tables and inserting data. 

[create_tables.py](https://github.com/sunnykan/sparkifydb_pg/blob/main/sparkifydb_pg/create_tables.py): Creates the database and the constituent tables.

[etl.py](https://github.com/sunnykan/sparkifydb_pg/blob/main/sparkifydb_pg/etl.py): Parses the data files, transforms the data and populates the tables in the database.
