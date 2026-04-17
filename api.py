import requests

API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

headers = {
    "x-apisports-key": API_KEY
}

def get_team_form(team_id):
    url = f"https://v3.football.api-sports.io/fixtures?team={team_id}&last=5"
    response = requests.get(url, headers=headers)
    data = response.json()

    goals_scored = 0
    goals_conceded = 0

    for match in data["response"]:
        goals_scored += match["goals"]["home"] if match["teams"]["home"]["id"] == team_id else match["goals"]["away"]
        goals_conceded += match["goals"]["away"] if match["teams"]["home"]["id"] == team_id else match["goals"]["home"]

    avg_scored = goals_scored / 5
    avg_conceded = goals_conceded / 5

    return avg_scored, avg_conceded
