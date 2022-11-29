import requests
import sys

refresh_token = " paste your refresh token here "
base_64 = " paste here base64 spotify ClientID : Client secret"

class Refresh:
    def refresh_token(self):

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": "Basic " + base_64})

        response_json = response.json()
        print(response_json)

