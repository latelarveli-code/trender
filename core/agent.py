def process_commercial_intent(title):
    t = title.lower()
    
    # Syvällisempi analyysi-logiikka
    if any(x in t for x in ["ai", "gpt", "neural"]):
        return {
            "type": "COGNITIVE AUTOMATION",
            "verdict": "Markkina on saturoitunut geneerisistä boteista. Fokusoi niche-integraatioihin.",
            "value": "KORKEA",
            "link": "https://www.google.com/search?q=ai+automation+consulting+niche"
        }
    elif any(x in t for x in ["code", "dev", "framework"]):
        return {
            "type": "INFRASTRUCTURE",
            "verdict": "Kehittäjien työkalujen kysyntä kasvaa. Mahdollisuus rakentaa 'shovels for gold miners'.",
            "value": "STABIILI",
            "link": "https://news.ycombinator.com"
        }
    return {
        "type": "EMERGING SIGNAL",
        "verdict": "Tunnistamaton markkinasignaali. Vaatii manuaalista validointia.",
        "value": "TUNTEMATON",
        "link": "https://www.google.com"
    }