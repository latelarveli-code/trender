def analyze_trade(title, pos_votes, neg_votes):
    t = title.lower()
    score = pos_votes - neg_votes
    
    analysis = {
        "call": "NEUTRAL",
        "logic": "Markkinasignaali on epäselvä.",
        "risk": "Keskitaso"
    }

    if score > 5 or any(x in t for x in ["bullish", "breakout", "listing", "pump"]):
        analysis.update({
            "call": "STRONG BUY",
            "logic": f"Vahva sosiaalinen konfirmosio (+{score}). Momentum kasvaa.",
            "risk": "Korkea"
        })
    elif score < -3 or any(x in t for x in ["scam", "hack", "dump", "bearish", "crash"]):
        analysis.update({
            "call": "STRONG SELL",
            "logic": f"Negatiivinen paine havaittu ({score}). Varautukaa laskuun.",
            "risk": "Erittäin Korkea"
        })
        
    return analysis