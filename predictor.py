import random

def analyze_match(team1, team2, form1, form2):

    score1 = form1 + random.uniform(0.5, 1.5)
    score2 = form2 + random.uniform(0.5, 1.5)

    total = score1 + score2

    if total > 3:
        pick = "Over 2.5"
    elif score1 > score2:
        pick = f"{team1} Win"
    else:
        pick = f"{team2} Win"

    confidence = round(random.uniform(85, 92), 1)

    score_prediction = f"{round(score1)}-{round(score2)}"

    return {
        "Pick": pick,
        "Confidence%": confidence,
        "Score": score_prediction
    }
