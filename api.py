import requests
from datetime import datetime
from config import API_KEY

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}


# 🟢 GET TODAY MATCHES
def get_today_matches():

    today = datetime.today().strftime("%Y-%m-%d")

    url = f"{BASE_URL}/fixtures?date={today}"

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

    except Exception as e:
        print("API ERROR (fixtures):", e)
        return []


# 🟢 TEAM STATS
def get_team_stats(team_id):

    url = f"{BASE_URL}/teams/statistics?season=2024&team={team_id}&league=39"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        stats = data.get("response", {})

        goals_for = stats.get("goals", {}).get("for", {}).get("average", {}).get("total", 1.2)
        goals_against = stats.get("goals", {}).get("against", {}).get("average", {}).get("total", 1.2)

        return {
            "goals_for": goals_for if goals_for else 1.2,
            "goals_against": goals_against if goals_against else 1.2
        }

    except Exception as e:
        print("API ERROR (stats):", e)
        return {
            "goals_for": 1.2,
            "goals_against": 1.2
        }


# 🟢 ODDS (VALUE BETTING CORE)
def get_match_odds(fixture_id):

    url = f"{BASE_URL}/odds?fixture={fixture_id}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        odds_data = data.get("response", [])

        if not odds_data:
            return None

        # أول bookmaker
        bookmakers = odds_data[0].get("bookmakers", [])

        if not bookmakers:
            return None

        bets = bookmakers[0].get("bets", [])

        if not bets:
            return None

        values = bets[0].get("values", [])

        if len(values) < 3:
            return None

        home_odds = float(values[0]["odd"])
        draw_odds = float(values[1]["odd"])
        away_odds = float(values[2]["odd"])

        return {
            "home": home_odds,
            "draw": draw_odds,
            "away": away_odds
        }

    except Exception as e:
        print("API ERROR (odds):", e)
        return None
