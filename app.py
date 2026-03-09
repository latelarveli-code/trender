import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Aalto-Vuo Innovation Scout", layout="wide")

st.title("🚀 Aalto-Vuo: Innovation Scout")
st.write("Skannataan maailman uusimpia teknologioita ja innovaatioita (Hacker News API).")

@st.cache_data(ttl=600)
def get_hacker_news_trends():
    # Haetaan parhaat tarinat
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(top_stories_url).json()[:20] # Haetaan 20 parasta
    
    trends = []
    for s_id in story_ids:
        s_url = f"https://hacker-news.firebaseio.com/v0/item/{s_id}.json"
        story = requests.get(s_url).json()
        if 'title' in story:
            trends.append({
                "Otsikko": story.title,
                "Linkki": story.get('url', f"https://news.ycombinator.com/item?id={s_id}"),
                "Pisteet": story.get('score', 0)
            })
    return pd.DataFrame(trends)

if st.sidebar.button("Skannaa Innovaatiot"):
    with st.spinner('Louhitaan dataa Hacker Newsista...'):
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
                        # Amazon-haku otsikon tärkeimmillä sanoilla
                        st.link_button("Amazon-haku", f"https://www.amazon.com/s?k={row['Otsikko']}")
                    with c3:
                        st.link_button("eBay-haku", f"https://www.ebay.com/sch/i.html?_nkw={row['Otsikko']}")
        else:
            st.error("Datan haku epäonnistui. Tarkista verkkoyhteys.")

st.sidebar.info("Hacker News on paikka, jossa tulevaisuuden trendit syntyvät. Jos näet täällä uuden ohjelmiston tai laitteen, se on pian suosittu kaikkialla.")