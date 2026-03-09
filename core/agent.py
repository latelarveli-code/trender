def process_commercial_intent(title):
    t = title.lower()
    # Oletusarvot
    meta = {
        "tag": "Innovaatio",
        "advice": "Tarkkaile markkinan kypsymistä.",
        "affiliate_url": "https://www.amazon.com?tag=OMA_TUNNUS-20", # Esimerkki
        "cta_text": "Hanki tarvikkeet"
    }
    
    if any(x in t for x in ["ai", "gpt", "model", "bot"]):
        meta.update({
            "tag": "AI-Automaatio",
            "advice": "Korkea kysyntä B2B-sektorilla. Rakenna MVP tästä.",
            "affiliate_url": "https://www.udemy.com/topic/ai-automation/",
            "cta_text": "Opettele AI-automaatio"
        })
    elif any(x in t for x in ["clean", "energy", "solar", "battery"]):
        meta.update({
            "tag": "Vihreä Tekno",
            "advice": "Valtiontuet ja ESG-raportointi ajavat tätä trendiä.",
            "affiliate_url": "https://www.ebay.com/b/Solar-Panels/",
            "cta_text": "Tutki komponentteja"
        })
    
    return meta