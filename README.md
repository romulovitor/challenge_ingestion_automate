# Integration automated

## Tasks
    - Create API
    - There must be an automated process to ingest and store the data.
    - Trips with similar origin, destination, and time of day should be grouped together.
    - Develop away to obtain the weekly average number of trips for an area,defined by a bounding box (given by coordinates) or by a region.
    - Develop a way to inform the user about the status of the data ingestion without using a polling solution
    - The solution should be scalable to 100 million entries. It is encouraged to simplify the data by a data model. Please add proof that the solution is scalable.
    - Use a SQL database.


## Background

We have provided a Github repo containing:

    A docker compose.yml file that configures a container for the MySQL database and the script
    A Dockerfile to build and run the python script
    A mysql-schemas folder containing a test.sql file. You can add your sql schemas here.



## Test

To ensure the database is up and running, the following test can be run:

docker-compose up --build test

## File to be analyse
- app/main.py (API)
- assesment/run.py (integration)
- query.sql (Query)


## API
Execute dockerfile inside the app folder
- acess API http://127.0.0.1:5000
- http://127.0.0.1:5000/status (verify status of data by the watermark)
- http://127.0.0.1:5000/group_by_three_way (using 'origin_coord', 'destination_coord', 'time_hour')
- http://127.0.0.1:5000/group_by_week 
- http://127.0.0.1:5000/sql_cheap_mobile
- http://127.0.0.1:5000/sql_rank_by_region


## Observation
- The test its not completed, but I have defined what expected from the final script.
- The solution it's not scalable, I'm using pandas to do the tratments, ideally could be use apache beam / Pyspark
- What is missing and how do this.
  - Store at database
    - Could use sqlalchemy
  - Make scalable
    - using a engine of distributed system like spark/hadoop ou apache beam from GCP
  - Make available the API endpoint
    - stablish the comunication beetwenn the API and database