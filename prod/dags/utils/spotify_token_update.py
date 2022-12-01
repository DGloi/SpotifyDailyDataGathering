import requests

refresh_token = " paste your refresh token here "
base_64 = " paste here base64(Client_ID:Client_secret) "

class Refresh:
    def refresh_token():

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": "Basic " + base_64})

        response_json = response.json()
        t = response_json.get("access_token")
        return t
