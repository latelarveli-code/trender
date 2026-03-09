import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

# Sivun asetukset
st.set_page_config(page_title="Aalto-Vuo Trend Hub", layout="wide")

st.title("🚀 Aalto-Vuo: Trendi- ja Kategoria-analyysi")
st.write("Valitse kategoria ja alue löytääksesi nousevat kaupalliset mahdollisuudet.")

# Kategoriat ja niiden koodit (Google Trends -standardi)
CATEGORIES = {
    "Kaikki": 0,
    "Teknologia": 5,
    "Terveys": 45,
    "Urheilu": 20,
    "Viihde": 3,
    "Bisnes & Talous": 12,
    "Lifestyle": 71,
    "Tiede": 174
}

# Käyttöliittymän asettelu (sivupalkki)
st.sidebar.header("Hakuehdot")
selected_region = st.sidebar.selectbox("Markkina-alue:", ["finland", "united_states", "sweden", "germany"])
selected_cat_name = st.sidebar.selectbox("Valitse kategoria:", list(CATEGORIES.keys()))
selected_cat_code = CATEGORIES[selected_cat_name]

# Funktio datan hakuun
@st.cache_data(ttl=1800)
def get_category_trends(region, category):
    try:
        pytrends = TrendReq(hl='fi-FI', tz=360)
        # Käytetään real-time trends jos mahdollista, tai trending_searches
        # Huom: Kaikki kategoriat eivät tue reaaliaikaista hakua kaikilla alueilla
        data = pytrends.trending_searches(pn=region)
        return data
    except Exception as e:
        return f"Virhe: {e}"

# Pääosio
if st.sidebar.button("Analysoi Markkinat"):
    with st.spinner('Louhitaan dataa...'):
        trends_df = get_category_trends(selected_region, selected_cat_code)
        
        if isinstance(trends_df, pd.DataFrame):
            st.success(f"Löytyi {len(trends_df)} nousevaa trendiä kategoriassa: {selected_cat_name}")
            
            # Luodaan ruudukko (grid) tuotteille
            cols = st.columns(2)
            for i, row in trends_df.iterrows():
                trend = row[0]
                with cols[i % 2]:
                    with st.container(border=True):
                        st.subheader(f"🔥 {trend}")
                        
                        # Automaattiset linkit
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.link_button("Etsi Amazonista", f"https://www.amazon.com/s?k={trend}")
                        with col_b:
                            st.link_button("Etsi eBaysta", f"https://www.ebay.com/sch/i.html?_nkw={trend}")
                        
                        st.markdown(f"**Vinkki:** Voit tehdä tästä aiheesta sisältöä tai etsiä halpoja eriä myytäväksi.")
        else:
            st.warning("Dataa ei juuri nyt saatavilla tällä valinnalla. Kokeile 'Kaikki' kategoriaa tai eri aluetta.")

# Lisäohjeet käyttäjälle
st.divider()
st.markdown("""
### 💡 Miten tästä saa rahaa?
Tämä työkalu on **päätöksentekokone**. Sen sijaan että arvaisit mitä myydä, se näyttää mitä ihmiset jo etsivät.
1. **Dropshipping:** Jos trendi on uusi tekninen vimpain, etsi toimittaja (esim. AliExpress) ja pystytä mainos.
2. **Affiliate Marketing:** Tee vertailuvideo tai blogi nousevasta aiheesta.
3. **Paikallinen arbitraasi:** Jos jokin vanha merkki nousee trendiksi (esim. "Retro Nokia"), etsi niitä käytettynä ja myy kalliimmalla.
""")