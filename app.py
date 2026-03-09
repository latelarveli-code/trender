import streamlit as st
import requests
import pandas as pd

# 1. Ulkoasuasetukset (Arkkitehtoninen minimalismi & Tumma teema)
st.set_page_config(page_title="Aalto-Vuo | Intelligence", layout="wide")

st.markdown("""
    <style>
    /* Taustan ja tekstin perusvärit */
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, span, label { color: #e6edf3 !important; font-family: 'Helvetica Neue', Arial, sans-serif; }
    
    /* Korttimainen ulkoasu trendeille */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
    }

    /* Metriikkalaatikot */
    div[data-testid="stMetric"] {
        background-color: #0d1117;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
    }

    /* Sivupalkin tyylittely */
    section[data-testid="stSidebar"] {
        background-color: #010409;
        border-right: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. AI-Agentin analyysilogiikka (Tämä on sovelluksen "aivot")
def ai_agent_analysis(title, score):
    # Luokitellaan trendi ja ehdotetaan liiketoimintamahdollisuutta
    title_lc = title.lower()
    
    analysis = {
        "priority": "KORKEA" if score > 150 else "NORMAALI",
        "category": "Yleinen innovaatio",
        "automation_potential": "Matala",
        "service_idea": "Seuraa teknologian kypsymistä."
    }
    
    if any(keyword in title_lc for keyword in ["ai", "gpt", "model", "learning", "neural"]):
        analysis["category"] = "Tekoäly & Koneoppiminen"
        analysis["automation_potential"] = "ERITTÄIN KORKEA"
        analysis["service_idea"] = "AI-agentin rakentaminen asiakasprosessin päälle."
    elif any(keyword in title_lc for keyword in ["tool", "workflow", "git", "automation", "script"]):
        analysis["category"] = "Työnkulun optimointi"
        analysis["automation_potential"] = "KORKEA"
        analysis["service_idea"] = "Toistuvien manuaalisten tehtävien automatisointi."
    elif any(keyword in title_lc for keyword in ["legal", "policy", "law", "copyright", "legitimate"]):
        analysis["category"] = "Säädökset & Juridiikka"
        analysis["automation_potential"] = "KOHTALAINEN"
        analysis["service_idea"] = "Automaattinen vaatimustenmukaisuus-tarkastus (Compliance)."
    elif any(keyword in title_lc for keyword in ["web", "framework", "js", "react", "html"]):
        analysis["category"] = "Verkkokehitys"
        analysis["automation_potential"] = "KORKEA"
        analysis["service_idea"] = "Skaalautuvat SaaS-arkkitehtuuripalvelut."

    return analysis

# 3. Datan haku
@st.cache_data(ttl=600)
def get_hacker_news_trends():
    try:
        # Haetaan parhaat tarinat (Top Stories)
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_stories_url, timeout=10)
        story_ids = response.json()[:12] # Haetaan 12 tuoreinta
        
        trends = []
        for s_id in story_ids:
            story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{s_id}.json", timeout=10).json()
            if story and 'title' in story:
                trends.append({
                    "id": s_id,
                    "title": story.get('title'),
                    "url": story.get('url', f"https://news.ycombinator.com/item?id={s_id}"),
                    "score": story.get('score', 0)
                })
        return pd.DataFrame(trends)
    except Exception as e:
        return pd.DataFrame()

# 4. Käyttöliittymän rakentaminen
st.title("AALTO-VUO | INNOVATION INTELLIGENCE")
st.write("---")

# Sivupalkin ohjaimet
st.sidebar.title("KOMENTOKESKUS")
st.sidebar.write("Project Aalto-Vuo v1.5")
if st.sidebar.button("KÄYNNISTÄ ANALYYSI", use_container_width=True):
    with st.spinner('Agentti louhii globaaleja signaaleja...'):
        df = get_hacker_news_trends()
        
        if not df.empty:
            for i, row in df.iterrows():
                # Ajetaan jokainen löydös AI-agentin läpi
                analysis = ai_agent_analysis(row['title'], row['score'])
                
                # Luodaan visuaalinen kortti jokaiselle trendille
                with st.container(border=True):
                    col_main, col_stats = st.columns([3, 1])
                    
                    with col_main:
                        st.subheader(row['title'])
                        st.write(f"**Kategoria:** {analysis['category']}")
                        st.info(f"💡 **AUTOMAATIO-IDEA:** {analysis['service_idea']}")
                        
                        # Napit
                        b1, b2 = st.columns(2)
                        with b1:
                            st.link_button("LUE LÄHDE", row['url'], use_container_width=True)
                        with b2:
                            st.link_button("MARKKINAHAKU", f"https://www.google.com/search?q={row['title']}+commercial+use", use_container_width=True)
                    
                    with col_stats:
                        st.metric("SUOSIO", row['score'], delta=analysis['priority'])
                        st.write("**Potentiaali:**")
                        st.write(analysis['automation_potential'])
        else:
            st.warning("Dataa ei saatu haettua. Tarkista yhteys.")

st.sidebar.divider()
st.sidebar.caption("Focus: Scalable Automation & Market Arbitrage")