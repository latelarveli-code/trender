def process_commercial_intent(title):
    t = title.lower()
    
    # Oletusarvot, jos mikään ehto ei täyty
    res = {
        "type": "EMERGING SIGNAL",
        "verdict": "Tunnistamaton markkinasignaali. Vaatii manuaalista validointia.",
        "value": "TUNTEMATON",
        "link": "https://www.google.com/search?q=" + title.replace(" ", "+")
    }
    
    # Analyysilogiikka
    if any(x in t for x in ["ai", "gpt", "neural", "intelligence"]):
        res.update({
            "type": "COGNITIVE AUTOMATION",
            "verdict": "Markkina on saturoitunut geneerisistä boteista. Fokusoi niche-integraatioihin.",
            "value": "KORKEA",
            "link": "https://www.google.com/search?q=ai+automation+consulting"
        })
    elif any(x in t for x in ["code", "dev", "framework", "rust", "python", "js"]):
        res.update({
            "type": "INFRASTRUCTURE",
            "verdict": "Kehittäjien työkalujen kysyntä kasvaa. Mahdollisuus rakentaa työkaluja ammattilaisille.",
            "value": "STABIILI",
            "link": "https://news.ycombinator.com"
        })
    elif any(x in t for x in ["money", "crypto", "pay", "fintech", "legal"]):
        res.update({
            "type": "SYSTEMIC VALUE",
            "verdict": "Regulaatio ja rahaliikenne muuttuvat. Korkea este markkinoille pääsyyn.",
            "value": "ERITTÄIN KORKEA",
            "link": "https://www.google.com/search?q=fintech+opportunities+2026"
        })
        
    return res