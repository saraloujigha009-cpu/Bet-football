import requests

API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?date=2026-04-17"
    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []

    for item in data["response"]:
        matches.append({
            "team1": item["teams"]["home"]["name"],
            "team2": item["teams"]["away"]["name"],
            "team1_id": item["teams"]["home"]["id"],
            "team2_id": item["teams"]["away"]["id"]
        })

    return matches
