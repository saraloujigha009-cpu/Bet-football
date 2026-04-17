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

        team1 = m["teams"]["home"]["name"]
        team2 = m["teams"]["away"]["name"]
        league = m["league"]["name"]

        matches.append({
            "team1": team1,
            "team2": team2,
            "league": league
        })

    return matches
