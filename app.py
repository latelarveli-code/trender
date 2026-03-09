import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

st.set_page_config(page_title="Aalto-Vuo Trend Hub", layout="wide")

st.title("🚀 Aalto-Vuo: Trendi-analyysi")
st.write("Jos data ei lataudu, kokeile vaihtaa aluetta (esim. United States on varmin).")

# Maiden koodit, jotka toimivat parhaiten
REGIONS = {
    "Suomi": "finland",
    "USA": "united_states",
    "Ruotsi": "sweden",
    "Saksa": "germany",
    "Iso-Britannia": "united_kingdom"
}

selected_region_name = st.sidebar.selectbox("Markkina-alue:", list(REGIONS.keys()))
selected_region = REGIONS[selected_region_name]

@st.cache_data(ttl=1200)
def get_safe_trends(region):
    try:
        # Lisätään timeout ja useita yrityksiä
        pytrends = TrendReq(hl='fi-FI', tz=360, timeout=(10,25))
        # Daily searches on paljon varmempi tapa saada dataa kuin kategoriat
        data = pytrends.trending_searches(pn=region)
        return data
    except Exception as e:
        return str(e)

if st.sidebar.button("Analysoi Markkinat"):
    with st.spinner('Haetaan tuoreimpia virtauksia...'):
        trends_df = get_safe_trends(selected_region)
        
        if isinstance(trends_df, pd.DataFrame):
            st.success(f"Löytyi päivän kuumimmat aiheet alueelta {selected_region_name}")
            
            # Näytetään tulokset nätisti
            for i, row in trends_df.iterrows():
                trend = row[0]
                with st.expander(f"🔥 {trend}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.link_button("Amazon", f"https://www.amazon.com/s?k={trend}")
                    with col2:
                        st.link_button("eBay", f"https://www.ebay.com/sch/i.html?_nkw={trend}")
                    with col3:
                        st.link_button("Google Search", f"https://www.google.com/search?q={trend}")
        else:
            st.error("Google Trends hylkäsi pyynnön. Tämä johtuu usein palvelimen IP-osoitteesta.")
            st.info("VINKKI: Kokeile USA-asetusta, se on vakain.")