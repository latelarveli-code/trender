import streamlit as st
import feedparser
import pandas as pd

st.set_page_config(page_title="Aalto-Vuo Trend Hub", layout="wide")

st.title("🚀 Aalto-Vuo: Trendi-analyysi (RSS-Varmistettu)")
st.write("Tämä versio käyttää RSS-syötteitä, jotka toimivat varmemmin pilvipalveluissa.")

# RSS-syötteiden osoitteet (Maa-koodit)
RSS_FEEDS = {
    "Suomi": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=FI",
    "USA": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US",
    "Saksa": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=DE",
    "Ruotsi": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=SE"
}

selected_region = st.sidebar.selectbox("Markkina-alue:", list(RSS_FEEDS.keys()))

def get_rss_trends(url):
    try:
        feed = feedparser.parse(url)
        trends = []
        for entry in feed.entries:
            # RSS-syötteessä on usein hakuvolyymi mukana
            trends.append({
                "Trendi": entry.title,
                "Kuvaus": entry.description,
                "Linkki": entry.link
            })
        return pd.DataFrame(trends)
    except Exception as e:
        return str(e)

if st.sidebar.button("Etsi Trendit"):
    with st.spinner('Haetaan RSS-dataa...'):
        df = get_rss_trends(RSS_FEEDS[selected_region])
        
        if isinstance(df, pd.DataFrame) and not df.empty:
            st.success(f"Löytyi {len(df)} kuumaa aihetta!")
            
            for i, row in df.iterrows():
                with st.expander(f"🔥 {row['Trendi']}"):
                    st.write(f"Analyysi: {row['Kuvaus']}")
                    
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.link_button("Amazon", f"https://www.amazon.com/s?k={row['Trendi']}")
                    with c2:
                        st.link_button("eBay", f"https://www.ebay.com/sch/i.html?_nkw={row['Trendi']}")
                    with c3:
                        st.link_button("Lue lisää", row['Linkki'])
        else:
            st.error("Datan haku epäonnistui RSS-reitilläkin. Google saattaa rajoittaa liikennettä juuri nyt.")

st.sidebar.info("Vinkki: Jos käytät puhelinta, kokeile virkistää sivu (Refresh).")