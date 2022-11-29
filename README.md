# SpotifyDailyDataGathering

This ETL project of mine allows to get all your recently played music and feed a database every few hours everyday with your listening history. I personnaly host this application on my local machine; with all the right credentials that it implies. 


This project is using the [Spotify API](https://developer.spotify.com/documentation/web-api/reference/#/) and connect to the API through Authorization Code Flow mode. Which means once set up properly, Apache Airflow will be able to run automatically without human interaction due to token expiration. 


## Technologies 

For this project, I have been using Python 3.6 and the following libraries :

* [pandas](https://pandas.pydata.org/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [sqlalchemy](https://pypi.org/project/SQLAlchemy/)
* [airflow](https://airflow.apache.org/docs/apache-airflow/2.1.4/installation/installing-from-pypi.html)

Aside from python , I personnaly use [DBeaver](https://dbeaver.io/), a free and open source database management program to run SQL queries on the created database afterwards.

All requirements for setting up a local environnement are to be found and run under requirements.txt


##  How can I set up this workflow on my machine ? 

The first thing you will need 
