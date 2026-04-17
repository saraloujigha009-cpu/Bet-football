def analyze_match(team1, team2, stats1, stats2):

    try:
        a1 = float(stats1.get("goals_for", 1.2))
        d1 = float(stats1.get("goals_against", 1.2))

        a2 = float(stats2.get("goals_for", 1.2))
        d2 = float(stats2.get("goals_against", 1.2))

        # xG model
        xg1 = (a1 + d2) / 2
        xg2 = (a2 + d1) / 2

        total = xg1 + xg2
        diff = abs(xg1 - xg2)

        # 🧠 decision system (NO RANDOM)
        if total >= 3.3:
            pick = "Over 2.5"

        elif diff < 0.2 and total >= 2.2:
            pick = "BTTS Yes"

        elif xg1 - xg2 >= 0.4:
            pick = f"{team1} Win"

        elif xg2 - xg1 >= 0.4:
            pick = f"{team2} Win"

        else:
            pick = "Under 2.5"

        # 🧠 confidence system (dynamic)
        confidence = 60 + (total * 10) + (diff * 15)

        if confidence > 92:
            confidence = 92

        return {
            "Pick": pick,
            "Confidence": round(confidence, 1),
            "Score": f"{round(xg1)}-{round(xg2)}"
        }

    except:
        return {
            "Pick": "No Bet",
            "Confidence": 0,
            "Score": "0-0"
        }
