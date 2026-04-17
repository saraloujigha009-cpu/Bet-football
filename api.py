import requests
from datetime import datetime
from config import API_KEY

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_today_matches():

    today = datetime.today().strftime("%Y-%m-%d")

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

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

    url = f"https://v3.football.api-sports.io/teams/statistics?season=2024&team={team_id}&league=39"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        stats = data.get("response", {})

        return {
            "goals_for": stats.get("goals", {}).get("for", {}).get("average", {}).get("total", 1.2) or 1.2,
            "goals_against": stats.get("goals", {}).get("against", {}).get("average", {}).get("total", 1.2) or 1.2
        }

    except:
        return {
            "goals_for": 1.2,
            "goals_against": 1.2
        }
