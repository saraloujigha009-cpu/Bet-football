import requests
from datetime import datetime
from config import API_KEY

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_today_matches():

    today = datetime.today().strftime("%Y-%m-%d")

    url = f"{BASE_URL}/fixtures?date={today}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        data = r.json()

        matches = []

        for m in data.get("response", []):

            matches.append({
                "fixture_id": m["fixture"]["id"],
                "team1": m["teams"]["home"]["name"],
                "team2": m["teams"]["away"]["name"],
                "team1_id": m["teams"]["home"]["id"],
                "team2_id": m["teams"]["away"]["id"],
                "league": m["league"]["name"]
            })

        return matches

    except:
        return []


def get_team_stats(team_id):

    url = f"{BASE_URL}/teams/statistics?season=2024&team={team_id}&league=39"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        data = r.json()

        stats = data.get("response", {})

        return {
            "goals_for": stats.get("goals", {}).get("for", {}).get("average", {}).get("total", 1.2),
            "goals_against": stats.get("goals", {}).get("against", {}).get("average", {}).get("total", 1.2)
        }

    except:
        return {"goals_for": 1.2, "goals_against": 1.2}


def get_match_odds(fixture_id):

    url = f"{BASE_URL}/odds?fixture={fixture_id}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        data = r.json()

        odds_data = data.get("response", [])

        if not odds_data:
            return None

        bookmakers = odds_data[0].get("bookmakers", [])
        bets = bookmakers[0].get("bets", [])
        values = bets[0].get("values", [])

        return {
            "home": float(values[0]["odd"]),
            "draw": float(values[1]["odd"]),
            "away": float(values[2]["odd"])
        }

    except:
        return None
