def analyze_opportunity(title):
    t = title.lower()
    # Tässä määritellään mihin ohjataan käyttäjä (Affiliate-mahdollisuus)
    analysis = {
        "category": "Innovaatio",
        "action_plan": "Tutki teknistä toteutusta.",
        "tool_link": "https://www.google.com/search?q=best+tools+for+" + title.replace(" ", "+")
    }
    
    if "ai" in t or "gpt" in t:
        analysis["category"] = "Tekoäly / Automaatio"
        analysis["action_plan"] = "Hyödynnä AI-rajapintoja prosessin tehostamiseen."
        # Esimerkki: Affiliate-linkki AI-kurssille
        analysis["tool_link"] = "https://www.udemy.com/courses/search/?q=ai+automation" 
    elif "web" in t or "app" in t:
        analysis["category"] = "Software Development"
        analysis["action_plan"] = "Skaalautuva pilvi-arkkitehtuuri on avainasemassa."
        analysis["tool_link"] = "https://www.bluehost.com/track/your-id" # Esimerkki hostaus-linkistä

    return analysis