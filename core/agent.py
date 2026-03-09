def analyze_trade(title, sentiment, price):
    t = title.lower()
    
    analysis = {
        "call": "HOLD",
        "logic": "Odotetaan vahvempaa signaalia.",
        "risk": "Keskitaso"
    }

    # Yksinkertainen mutta tehokas logiikka
    if sentiment > 10 or any(x in t for x in ["bullish", "launch", "breakout", "listing"]):
        analysis.update({
            "call": "HOT BUY",
            "logic": "Vahva positiivinen sentimentti ja uutisajuri.",
            "risk": "Korkea (Momentum)"
        })
    elif any(x in t for x in ["hack", "scam", "bearish", "crash", "sec"]):
        analysis.update({
            "call": "DUMP / SHORT",
            "logic": "Negatiivinen uutissignaali havaittu.",
            "risk": "Erittäin korkea"
        })

    return analysis