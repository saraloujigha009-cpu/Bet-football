import requests
from datetime import datetime
from config import API_KEY

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_today_matches():

    today = datetime.today().strftime("%Y-%m-%d")

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    response = requests.get(url, headers=HEADERS)
    data = response.json()

    matches = []

    for m in data["response"]:

        matches.append({
            "fixture_id": m["fixture"]["id"],

            "team1": m["teams"]["home"]["name"],
            "team2": m["teams"]["away"]["name"],

            "team1_id": m["teams"]["home"]["id"],
            "team2_id": m["teams"]["away"]["id"],

            "league": m["league"]["name"]
        })

    return matches
