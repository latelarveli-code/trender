import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Aalto-Vuo Innovation Scout", layout="wide")

st.title("🚀 Aalto-Vuo: Innovation Scout")
st.write("Skannataan maailman uusimpia teknologioita ja innovaatioita (Hacker News API).")

@st.cache_data(ttl=600)
def get_hacker_news_trends():
    try:
        # Haetaan parhaat tarinat
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_stories_url, timeout=10)
        story_ids = response.json()[:20] 
        
        trends = []
        for s_id in story_ids:
            s_url = f"https://hacker-news.firebaseio.com/v0/item/{s_id}.json"
            story = requests.get(s_url, timeout=10).json()
            
            if story and 'title' in story:
                trends.append({
                    "Otsikko": story.get('title', 'Ei otsikkoa'),
                    "Linkki": story.get('url', f"https://news.ycombinator.com/item?id={s_id}"),
                    "Pisteet": story.get('score', 0)
                })
        return pd.DataFrame(trends)
    except Exception as e:
        st.error(f"Yhteysvirhe: {e}")
        return pd.DataFrame()

if st.sidebar.button("Skannaa Innovaatiot"):
    with st.spinner('Louhitaan dataa...'):
        df = get_hacker_news_trends()
        
        if not df.empty:
            st.success(f"Löytyi {len(df)} nousevaa innovaatiota!")
            for i, row in df.iterrows():
                with st.container(border=True):
                    st.subheader(f"💡 {row['Otsikko']}")
                    st.write(f"Suosioindeksi: {row['Pisteet']} pistettä")
                    
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.link_button("Lue artikkeli", row['Linkki'])
                    with c2:
                        st.link_button("Amazon-haku", f"https://www.amazon.com/s?k={row['Otsikko']}")
                    with c3:
                        st.link_button("eBay-haku", f"https://www.ebay.com/sch/i.html?_nkw={row['Otsikko']}")
        else:
            st.warning("Dataa ei saatu haettua. Kokeile painaa nappia uudelleen.")