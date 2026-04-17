from api import get_today_matches, get_team_stats
from predictor import analyze_match
from telegram import Update
from telegram.ext import ContextTypes


def smart_pick(xg1, xg2, total):

    # 🧠 logic ذكي حسب الأرقام
    if total >= 3.2:
        return "Over 2.5"
    elif abs(xg1 - xg2) < 0.3:
        return "BTTS Yes"
    elif xg1 > xg2:
        return "Home Win"
    else:
        return "Away Win"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    matches = get_today_matches()

    bets = []

    for m in matches[:15]:

        try:
            stats1 = get_team_stats(m["team1_id"])
            stats2 = get_team_stats(m["team2_id"])

            attack1 = float(stats1.get("goals_for", 1.2))
            defense1 = float(stats1.get("goals_against", 1.2))

            attack2 = float(stats2.get("goals_for", 1.2))
            defense2 = float(stats2.get("goals_against", 1.2))

            xg1 = (attack1 + defense2) / 2
            xg2 = (attack2 + defense1) / 2

            total = xg1 + xg2

            pick = smart_pick(xg1, xg2, total)

            confidence = 70 + abs(xg1 - xg2) * 12

            if confidence > 92:
                confidence = 92

            bets.append({
                "team1": m["team1"],
                "team2": m["team2"],
                "pick": pick,
                "confidence": round(confidence, 1)
            })

        except:
            continue

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    msg = "🔥 SMART VALUE BETS\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Prediction: {b['pick']}
Confidence: {b['confidence']}%
"""

    await update.message.reply_text(msg)
