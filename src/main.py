#Importing needed libraries
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3
import pandas as pd


DATA_LOCATION = "sqlite://whatdoilistento.sqlite"
USER_ID = "1154451207"
TOKEN = "BQCrZiDn_I-8vs1SaVYJPxvWzSC3thw4vkpUzUZoHrEREoYXQocZkE2rG1hwnSigsxA9viKcU4WH4oLNIcS_MtKJq9SSpNHBeJCYNlhJFJ5gsM997pb-Ak7-JJCICFV25zmBOW08mMD205xKuEKDn4NAsSS7v9-rksXImkmYfVukz6Gt8bH2"

if __name__ == "__main__":

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
    release_dates= []
    albums_list= []
    timestamps= []

for song in data["items"]:
    song_names.append(song["track"]["name"])
    artist_names.append(song["track"]["artists"][0]["name"])
    played_at_list.append(song["played_at"])
    release_dates.append(song["track"]["album"]["release_date"]) 
    albums_list.append(song["track"]["album"]["name"])
    timestamps.append(song["played_at"][0:10])

data_dict = {
    "song_name" : song_names,
    "album" : albums_list,
    "released_date" : release_dates,
    "artist" : artist_names,
    "played_at" : played_at_list,
    "timestamp" : timestamps
}

data_df=pd.DataFrame(
    data_dict,columns=["song_name","album","released_date","artist","played_at","timestamp"])

print(data_df)