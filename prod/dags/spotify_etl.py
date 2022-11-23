#Importing needed libraries
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3
import pandas as pd

from utils.check_valid_data import check_import
from utils.spotify_token_update import spotify_token

DATA_LOCATION = "sqlite:////Users/doriangloinec/Documents/GitHub/SpotifyDailyDataGathering/prod/data/what_do_i_listen_to.sqlite"
USER_ID = "1154451207"
TOKEN = "BQBfq0RuDqx3dMnr4Ve_khvvk12eTN5tEbSiWA00_Jqy3PXY226NC-JQcW3WmQIyghtiU8PLox_TfMWEGychnqruGURlqB5y1-Ky_i-ERhVgdGGcPRvW_O95ukz88NalMaG2BSd309DvsVnlEIsildcs3UoUylfgSC9JUjvlU2dl6RSz09zg"


def run_spotify_etl():

    headers = {
        "Accept":"application/json",
        "Content-type":"application/json",
        "Authorization":"Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 1)

    #unix time unit in ms as per API requierements
    unix_yesterday = int(yesterday.timestamp() * 1000)

    r = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(
            time=unix_yesterday),headers=headers)
    
    data = r.json()
    #f = open('/Users/doriangloinec/Documents/GitHub/SpotifyDailyDataGathering/src/data.json')
    #with open("data.json", 'w') as f:
        #json.dump(data, f)

    song_names = [] 
    artist_names = []
    played_at_list = []
    release_dates = []
    albums_list = []
    day_played_list = []
    hour_played_list = []
    

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        release_dates.append(song["track"]["album"]["release_date"]) 
        albums_list.append(song["track"]["album"]["name"])
        day_played_list.append(song["played_at"][0:10])
        hour_played_list.append(song["played_at"][12:16])

    data_dict = {
        "song_name" : song_names,
        "album" : albums_list,
        "released_date" : release_dates,
        "artist" : artist_names,
        "played_at" : played_at_list,
        "day_played" : day_played_list,
        "hour_played" : hour_played_list
    }

    data_df = pd.DataFrame(
        data_dict,columns = ["song_name","album","released_date","artist","played_at","day_played","hour_played"])

    #data quality check
    if check_import(data_df):
        print("Data from spotify passed the quality check, loading to database..")
    
    #Load
    engine = sqlalchemy.create_engine(DATA_LOCATION)
    connection = sqlite3.connect("what_do_i_listen_to.sqlite")
    cursor = connection.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        album VARCHAR(200),
        released_date VARCHAR(200),
        artist VARCHAR(200),
        played_at VARCHAR(200),
        day_played VARCHAR(200),
        hour_played VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)    
    )
    """

    cursor.execute(sql_query)
    print("database opened successfully")

    try:
        data_df.to_sql("my_played_tracks",engine,index=False, if_exists="append")
    except Exception as e:
        print("There was an issue loading the data. " + str(e))
    
    connection.close()
    print("database connection closed succcesfully")

