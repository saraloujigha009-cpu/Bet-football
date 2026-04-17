import requests
from datetime import datetime

API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

def get_today_matches():

    today = datetime.today().strftime('%Y-%m-%d')

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    headers = {
        "x-apisports-key": API_KEY
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    matches = []

    for m in data["response"]:

        matches.append({
            "team1": m["teams"]["home"]["name"],
            "team2": m["teams"]["away"]["name"]
        })

    return matches
