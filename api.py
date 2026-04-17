import requests

API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

headers = {"x-apisports-key": API_KEY}

def get_form(team_id):

    url = f"https://v3.football.api-sports.io/fixtures?team={team_id}&last=5"
    res = requests.get(url, headers=headers)
    data = res.json()

    goals_scored = 0
    goals_conceded = 0
    wins = 0

    for m in data["response"]:

        home_id = m["teams"]["home"]["id"]
        away_id = m["teams"]["away"]["id"]

        home_goals = m["goals"]["home"]
        away_goals = m["goals"]["away"]

        if team_id == home_id:
            goals_scored += home_goals
            goals_conceded += away_goals
            if home_goals > away_goals:
                wins += 1
        else:
            goals_scored += away_goals
            goals_conceded += home_goals
            if away_goals > home_goals:
                wins += 1

    return {
        "avg_scored": goals_scored / 5,
        "avg_conceded": goals_conceded / 5,
        "win_rate": wins / 5
    }
