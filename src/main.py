
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
TOKEN = "BQCjoa_OKXEaMSAOcmxQ-ZdWKTz8GbuaunlTw4LpSdzUxOO8kUmQMCLLMViuGRcuJxG30W4JzDGE1zWdM1xcN4ZCHQKj7ms-PcmWa-bobg8wrL7RCQ6M-lbCwy_ePDn-wwJswPT7EQmNUwRrLK_L8-NElvz9kaZS4RiW9FG1hKtHpdicK4Oc"

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

    song_names = []  #darude-sandstrom
    artist_names = []
    played_at_list = []
    release_dates= []
    albums_list= []
    timestamps= []

for song in data["items"]:
    song_names.append(song["track"]["name"])
    artist_names.append(song["track"]["album"]["artists"][0]["name"])
    played_at_list.append(song["played_at"])
    release_dates.append(song["release_date"])
    timestamps.append(song["played_at"][0:10])

data_dict = {
    "song_name" : song_names,
    "artist_" : artist_names,
    "played at" : played_at_list,
    "timestamp" : timestamps
}

print(data_dict)
