
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
USER_ID = "Dorian"
TOKEN = "TOKEN"

if __name__ == "__main__":

    header = {
        "Accept":"application/json",
        "Content-type":"application/json",
        "Authorization":"Bearer {token}".format(token=TOKEN)
    }
    today= datetime.datetime.now()
    yesterday=today-datetime.timedelta(days=1)
    unix_yesterday=int(yesterday.timestamp()*1000)
    
    
