def get_match_odds(fixture_id):

    url = f"https://v3.football.api-sports.io/odds?fixture={fixture_id}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        odds_data = data.get("response", [])

        if not odds_data:
            return None

        # ناخدو 1X2 market
        bookmakers = odds_data[0]["bookmakers"][0]["bets"][0]["values"]

        home_odds = float(bookmakers[0]["odd"])
        draw_odds = float(bookmakers[1]["odd"])
        away_odds = float(bookmakers[2]["odd"])

        return {
            "home": home_odds,
            "draw": draw_odds,
            "away": away_odds
        }

    except:
        return None
