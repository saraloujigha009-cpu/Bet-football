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


def get_team_stats(team_id):

    url = f"https://v3.football.api-sports.io/teams/statistics?season=2024&team={team_id}&league=39"

    response = requests.get(url, headers=HEADERS)
    data = response.json()

    try:
        stats = data["response"]

        goals_for = stats["goals"]["for"]["average"]["total"]
        goals_against = stats["goals"]["against"]["average"]["total"]

        return {
            "goals_for": goals_for if goals_for else 1.2,
            "goals_against": goals_against if goals_against else 1.2
        }

    except:
        return {
            "goals_for": 1.2,
            "goals_against": 1.2
        }
