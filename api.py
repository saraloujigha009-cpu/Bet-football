import requests

API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

url = "https://v3.football.api-sports.io/fixtures?date=2026-04-17"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)
data = response.json()

matches = []

for item in data["response"]:
    matches.append({
        "team1": item["teams"]["home"]["name"],
        "team2": item["teams"]["away"]["name"],
        "team1_avg_goals": 1.2,
        "team2_avg_goals": 1.1
    })
