
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
TOKEN = "BQCJCosalqWWa5keHMbuvIAeP0bcRsHfDnZ2yz0liuCdb3RBeJCV5Fb4R_X-bmKnIhbrwl9734ezqrVJhMKDsBGMQSRxJvxdqczXi-kCrBQnz5CcgGEDB4REN2lwL_MM4yXQwav25lbo9FGM_pj7sEL2Hgq2lAkYUhN3Qolzn-afXXnhjj-R"

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
    print(data)

    song_names = []  #darude-sandstrom
    artist_names = []
    played_at_list = []
    release_dates= []
    albums_list= []
    timetamp= []

    for song in data:
        song_names.append

