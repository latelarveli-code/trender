import streamlit as st
import requests
import pandas as pd

# 1. Ulkoasuasetukset (Arkkitehtoninen minimalismi)
st.set_page_config(page_title="Aalto-Vuo | Intelligence", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stSecondaryBlock { background-color: #1a1c23; }
    h1 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 200; color: #ffffff; }
    .stMetric { background-color: #161b22; border-radius: 5px; padding: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("AALTO-VUO | INNOVATION INTELLIGENCE")
st.write("Analysoidaan globaaleja signaaleja ja kaupallisia automaatiomahdollisuuksia.")

# 2. AI-Agentin analyysilogiikka
def ai_agent_analysis(title, score):
    # Simuloitu agentti, joka antaa strategisia neuvoja otsikon perusteella
    analysis = {
        "score_level": "Korkea" if score > 150 else "Vakaa",
        "action": "Tarkkaile kehitystä",
        "service_idea": "Prosessi-automaatio"
    }
    
    title_lc = title.lower()
    if "ai" in title_lc or "learning" in title_lc:
        analysis["service_idea"] = "AI-integraatio olemassa olevaan asiakasdataan."
    elif "tool" in title_lc or "language" in title_lc:
        analysis["service_idea"] = "Kehitysympäristön automaatio ja workflow-optimointi."
    elif "legal" in title_lc or "policy" in title_lc:
        analysis["service_idea"] = "Säädöstenmukaisuuden (Compliance) seuranta-agentti."
    
    return analysis

@st.cache_data(ttl=600)
def get_hacker_news_trends():
    try:
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        story_ids = requests.get(top_stories_url, timeout=10).json()[:15]
        
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
    except:
        return pd.DataFrame()

# 3. Pääkäyttöliittymä
if st.sidebar.button("KÄYNNISTÄ SKANNAUS"):
    with st.spinner('Agentti skannaa verkkoa...'):
        df = get_hacker_news_trends()
        
        if not df.empty:
            for i, row in df.iterrows():
                analysis = ai_agent_analysis(row['title'], row['score'])
                
                # Visualisointi korteissa
                with st.container(border=True):
                    col_text, col_metrics = st.columns([3, 1])
                    
                    with col_text:
                        st.subheader(row['title'])
                        st.caption(f"Lähde: Hacker News | ID: {row['id']}")
                        st.markdown(f"**AI Agentin ehdotus:** *{analysis['service_idea']}*")
                        
                        c1, c2 = st.columns(2)
                        with c1:
                            st.link_button("LUE ALKUPERÄINEN", row['url'], use_container_width=True)
                        with c2:
                            st.link_button("AMAZON TRENDS", f"https://www.amazon.com/s?k={row['title']}", use_container_width=True)
                    
                    with col_metrics:
                        st.metric("Pisteet", row['score'], delta=f"{analysis['score_level']} priorit")
                        st.write("---")
                        st.write(f"**Status:** {analysis['action']}")
        else:
            st.warning("Yhteys katkesi. Yritä uudelleen.")

st.sidebar.divider()
st.sidebar.markdown("### AALTO-VUO PROTOTYPE V1.5")
st.sidebar.write("Fokus: Low-cost automaatiopalvelut ja skaalautuvuus.")