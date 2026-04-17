def analyze_match(team1, team2, stats1, stats2):

    try:
        attack1 = float(stats1.get("goals_for", 1.2))
        defense1 = float(stats1.get("goals_against", 1.2))

        attack2 = float(stats2.get("goals_for", 1.2))
        defense2 = float(stats2.get("goals_against", 1.2))

        # 🧠 expected goals model
        xg1 = (attack1 + defense2) / 2
        xg2 = (attack2 + defense1) / 2

        total = xg1 + xg2

        # 🟢 probability estimation
        prob_team1 = xg1 / (xg1 + xg2)
        prob_team2 = xg2 / (xg1 + xg2)

        # 🟢 decision logic (value based)
        if total >= 3.0:
            pick = "Over 2.5"
            confidence = total * 25

        elif prob_team1 > 0.60:
            pick = f"{team1} Win"
            confidence = prob_team1 * 100

        elif prob_team2 > 0.60:
            pick = f"{team2} Win"
            confidence = prob_team2 * 100

        else:
            pick = "BTTS Yes"
            confidence = 70

        if confidence > 92:
            confidence = 92

        score = f"{round(xg1)}-{round(xg2)}"

        return {
            "Pick": pick,
            "Confidence": round(confidence, 1),
            "Score": score
        }

    except:
        return {
            "Pick": "No Bet",
            "Confidence": 0,
            "Score": "0-0"
        }
