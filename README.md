# SpotifyDailyDataGathering

This ETL project of mine allows to get all your recently played music and feed a database every few hours everyday with your listening history. I personnaly host this application on my local machine; with all the right credentials that it implies. 


This project is using the [Spotify API](https://developer.spotify.com/documentation/web-api/reference/#/) and connect to the API through Authorization Code Flow mode. Which means once set up properly, Apache Airflow will be able to run automatically without any token expiration issues. 


## Technologies

For this project, I have been using Python 3.6 and the following libraries :

* [pandas](https://pandas.pydata.org/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [sqlalchemy](https://pypi.org/project/SQLAlchemy/)
* [airflow](https://airflow.apache.org/docs/apache-airflow/2.1.4/installation/installing-from-pypi.html)

Aside from python , I personnaly use [DBeaver](https://dbeaver.io/), a free and open source database management program to run SQL queries on the created database afterwards.

All requirements for setting up a local environnement are to be found and run under ***requirements.txt***


## How can I set up this workflow on my machine ?

### <ins>1. Setting up spotify account and api requirements.<ins>

The first thing you will need is to have a Spotify account. Once this is done, you need to connect to it [here](https://developer.spotify.com/dashboard/login) and register your local instance of this application.
 
<p align="center">
<img width="205" alt="Screenshot 2022-11-29 at 19 11 28" src="https://user-images.githubusercontent.com/93589158/204612667-eadc845f-0c52-435b-abcc-badd6937bc37.png">
<p>
This should provide a Client Id and a Client Secret that we will need get tokens to have acces to the API.
While registering the application on spotify api website, it is important to specify a website uri to get our token update.
Find : [Spotify API connection process](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)

Once you have the following : 
* Application's Client ID
* Application's Client Secret
* Application's refresh token
* Your personnal spotify account ID

 You can go to the next step.
 
 ### <ins> 2. Setting up python files to your local machine with your credentials <ins>
 
 Because credential as sensible information, its better to set up this application on your local machine or, if you feel like, in your docker account although it will require some adaptation on your end. 
 
A few files need to be fed with you credentials.

i. In **prod/dags/utils/spotify_token_update.py**, fill the variable refresh_token with the refresh token you get from spotify api callback url.
You also need to fill the variable base_64 with a base64 conversion of the following (your_client_id:your_client_secret)

ii. In **prod/dags/spotify_etl.py**, in the variable data_location you would have to put a local path from your machine but keep the formating. 


 ### <ins>3. Setting up Apache Airflow.  <ins>

You should normally have airflow from the **requirement.txt**, but in case you didnt use it, please intall it with pypi.
```python
# install from pypi using pip
pip install apache-airflow
```

Once airflow is installed, launch the following command in your virtual environnement  
```python
airflow standalone

# Visit localhost:8080 in the browser and use the admin account details to be found in the airflow main folder after installation.
# shown on the terminal to login.
# Enable the example_bash_operator dag in the home page

```
After installation, you can visit airflow's folder and open config file to redirect the dag folder to **prod/dags/spotify_dag.py**  .
That way, airflow will be able to locate the workflow we prepared to get our tracks.
 
 If you connect from your browser to 
 ```
 localhost:8080
 ```

---

## <ins> Contributors <ins>

Dorian Gloinec

Email: dorian.gloinec@protonmail.com

LinkedIn: https://www.linkedin.com/in/dorian-gloinec/
