def analyze_match(team1, team2, stats1, stats2):

    # 🟢 القوة الهجومية والدفاعية
    attack1 = float(stats1["goals_for"])
    defense1 = float(stats1["goals_against"])

    attack2 = float(stats2["goals_for"])
    defense2 = float(stats2["goals_against"])

    # 🧠 توقع الأهداف (simple xG model)
    xg1 = (attack1 + defense2) / 2
    xg2 = (attack2 + defense1) / 2

    total_goals = xg1 + xg2

    # 🟢 اختيار التوقع
    if total_goals >= 3:
        pick = "Over 2.5"
    elif xg1 > xg2 + 0.3:
        pick = f"{team1} Win"
    elif xg2 > xg1 + 0.3:
        pick = f"{team2} Win"
    else:
        pick = "BTTS Yes"

    # 🟢 confidence منطقي (ماشي random)
    confidence = 70 + abs(xg1 - xg2) * 15

    if confidence > 92:
        confidence = 92

    score = f"{round(xg1)}-{round(xg2)}"

    return {
        "Pick": pick,
        "Confidence": round(confidence, 1),
        "Score": score
    }
