def analyze_match(team1, team2, stats1, stats2, odds=None):

    try:
        a1 = float(stats1.get("goals_for", 1.2))
        d1 = float(stats1.get("goals_against", 1.2))
        a2 = float(stats2.get("goals_for", 1.2))
        d2 = float(stats2.get("goals_against", 1.2))

        xg1 = (a1 + d2) / 2
        xg2 = (a2 + d1) / 2

        total = xg1 + xg2
        diff = abs(xg1 - xg2)

        p1 = xg1 / (xg1 + xg2)
        p2 = xg2 / (xg1 + xg2)

        # decision
        if total >= 3.4:
            pick = "Over 2.5"
            prob = total / 5

        elif p1 > 0.62:
            pick = f"{team1} Win"
            prob = p1

        elif p2 > 0.62:
            pick = f"{team2} Win"
            prob = p2

        else:
            pick = "BTTS Yes"
            prob = 0.55

        # VALUE
        if odds:
            if "Home" in pick:
                implied = 1 / odds["home"]
            elif "Away" in pick:
                implied = 1 / odds["away"]
            else:
                implied = 0.5

            value = (prob - implied) * 100
        else:
            value = prob * 100

        confidence = 50 + value + (total * 5)

        if confidence > 95:
            confidence = 95

        return {
            "Pick": pick,
            "Confidence": round(confidence, 1),
            "Value": round(value, 1),
            "Score": f"{round(xg1)}-{round(xg2)}"
        }

    except:
        return {"Pick": "No Bet", "Confidence": 0, "Value": 0, "Score": "0-0"}
