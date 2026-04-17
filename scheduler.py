from api import get_matches
from predictor import analyze_match
from bot import send_message

def send_daily_bets():

    matches = get_matches()
    bets = []

    for m in matches:

        result = analyze_match(
            m["team1"],
            m["team2"],
            m["team1_form"][0],
            m["team2_form"][0]
        )

        if result["Confidence%"] >= 80:
            bets.append({
                "match": f"{m['team1']} vs {m['team2']}",
                "result": result
            })

    # ترتيب من الأقوى
    bets.sort(key=lambda x: x["result"]["Confidence%"], reverse=True)

    # نخليو غير top 3
    top_bets = bets[:3]

    if not top_bets:
        send_message("❌ No strong bets today")
        return

    msg = "🔥 TODAY BEST 3 BETS 🔥\n\n"

    for i, b in enumerate(top_bets, start=1):
        r = b["result"]

        msg += f"""
{i}. {b['match']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}

"""

    send_message(msg)
