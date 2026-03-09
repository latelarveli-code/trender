import streamlit as st
import feedparser
import pandas as pd

st.set_page_config(page_title="Aalto-Vuo Reddit Hunter", layout="wide")

st.title("🤖 Aalto-Vuo: Reddit Trend Hunter")
st.write("Skannataan Redditin kuumimmat puheenaiheet suoraan lähteestä.")

# Valittavat kategoriat (Subredditit)
SUBREDDITS = {
    "Teknologia (r/technology)": "technology",
    "Vimpaimet (r/gadgets)": "gadgets",
    "Pelaaminen (r/gaming)": "gaming",
    "Tiede (r/science)": "science",
    "Kaikki (r/all)": "all"
}

selected_sub = st.sidebar.selectbox("Valitse kanava:", list(SUBREDDITS.keys()))

def get_reddit_trends(subreddit):
    # Redditin RSS-osoite
    url = f"https://www.reddit.com/r/{subreddit}/hot/.rss"
    # Reddit vaatii uniikin User-Agentin, jotta se ei blokkaa pyyntöä
    feed = feedparser.parse(url, agent='AaltoVuoBot/1.0')
    
    trends = []
    for entry in feed.entries:
        trends.append({
            "Otsikko": entry.title,
            "Linkki": entry.link,
            "Päivitetty": entry.updated
        })
    return pd.DataFrame(trends)

if st.sidebar.button("Skannaa Keskustelut"):
    with st.spinner(f'Haetaan tietoa kanavalta {selected_sub}...'):
        df = get_reddit_trends(SUBREDDITS[selected_sub])
        
        if not df.empty:
            st.success(f"Löytyi {len(df)} kuumaa keskustelua!")
            
            for i, row in df.iterrows():
                with st.expander(f"💬 {row['Otsikko']}"):
                    st.write(f"Julkaistu: {row['Päivitetty']}")
                    
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        # Amazon-haku otsikon perusteella
                        st.link_button("Etsi Amazonista", f"https://www.amazon.com/s?k={row['Otsikko']}")
                    with c2:
                        # eBay-haku
                        st.link_button("Etsi eBaysta", f"https://www.ebay.com/sch/i.html?_nkw={row['Otsikko']}")
                    with c3:
                        # Alkuperäinen Reddit-ketju
                        st.link_button("Lue Redditissä", row['Linkki'])
        else:
            st.error("Reddit ei vastannut pyyntöön. Yritä hetken kuluttua uudelleen.")

st.sidebar.markdown("---")
st.sidebar.info("Reddit-trendit paljastavat kuluttajien kiinnostuksen kohteet ennen kuin ne näkyvät kauppojen hyllyillä.")