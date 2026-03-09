import streamlit as st
import requests
import pandas as pd
import base64

# 1. Ulkoasu (Architect Dark Gold - Teema, joka viestii arvokkuutta)
st.set_page_config(page_title="Aalto-Vuo | Commercial Intelligence", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 300; color: #d4af37 !important; }
    p, span { color: #cfd8dc !important; }
    
    .stButton>button {
        background-color: #d4af37;
        color: #0b0d11;
        border-radius: 2px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f1c40f;
        transform: translateY(-2px);
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #151921;
        border: 1px solid #2d333b;
        border-radius: 4px;
        padding: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Kaupallinen AI-Agentti
def commercial_agent_analysis(title, score):
    title_lc = title.lower()
    
    # Perusanalyysi
    analysis = {
        "strategy": "Arbitraasi / Tiedon myynti",
        "monetization": "Luo sisältöä tai opas",
        "urgency": "Matala",
        "target_audience": "Yleinen"
    }
    
    # Kaupalliset triggerit
    if any(k in title_lc for k in ["ai", "gpt", "bot", "automate"]):
        analysis["strategy"] = "SaaS / B2B Automaatio"
        analysis["monetization"] = "Myy integraatiopalvelua yrityksille"
        analysis["urgency"] = "ERITTÄIN KORKEA"
        analysis["target_audience"] = "Pk-yritykset"
    elif any(k in title_lc for k in ["law", "legal", "tax", "policy"]):
        analysis["strategy"] = "Konsultointi / Compliance"
        analysis["monetization"] = "Automaattinen auditointi-työkalu"
        analysis["urgency"] = "KRIITTINEN"
        analysis["target_audience"] = "Laki- ja talousosastot"
    elif any(k in title_lc for k in ["tool", "framework", "library", "app"]):
        analysis["strategy"] = "Affiliate / Kurssit"
        analysis["monetization"] = "Tee tutoriaali ja käytä affiliate-linkkejä"
        analysis["urgency"] = "KESKITASO"
        analysis["target_audience"] = "Kehittäjät"

    return analysis

# 3. Datan haku (Hacker News)
@st.cache_data(ttl=600)
def get_trends():
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        ids = requests.get(url, timeout=10).json()[:10]
        data = []
        for i in ids:
            item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json").json()
            if item and 'title' in item:
                data.append({
                    "title": item['title'],
                    "url": item.get('url', f"https://news.ycombinator.com/item?id={i}"),
                    "score": item.get('score', 0)
                })
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# 4. Raportin generointi (CSV-vienti rahanarvoista tietoa varten)
def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="aalto_vuo_report.csv" style="color: #d4af37; text-decoration: none; border: 1px solid #d4af37; padding: 10px; border-radius: 5px;">LATAA MARKKINARAPORTTI (CSV)</a>'

# 5. Päänäkymä
st.title("AALTO-VUO | COMMERCIAL INTELLIGENCE")
st.write("Tunnista markkinarakot ennen muita.")

st.sidebar.title("KOMENTOKESKUS")
if st.sidebar.button("SKANNAA TUOTTO-MAHDOLLISUUDET", use_container_width=True):
    trends_df = get_trends()
    
    if not trends_df.empty:
        st.markdown(get_csv_download_link(trends_df), unsafe_allow_html=True)
        st.write("") # Väli
        
        for i, row in trends_df.iterrows():
            biz = commercial_agent_analysis(row['title'], row['score'])
            
            with st.container(border=True):
                c1, c2 = st.columns([2, 1])
                
                with c1:
                    st.subheader(row['title'])
                    st.write(f"🎯 **Strategia:** {biz['strategy']}")
                    st.write(f"💰 **Miten teet rahaa:** {biz['monetization']}")
                    
                    # Kaupalliset toimintanapit
                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        st.link_button("TARKISTA KILPAILU (Google)", f"https://www.google.com/search?q={row['title']}+competitors")
                    with btn_col2:
                        st.link_button("ETSI TYÖKALUT (Udemy)", f"https://www.udemy.com/courses/search/?q={row['title']}")
                
                with c2:
                    st.metric("KIIRELLISYYS", biz['urgency'])
                    st.write(f"**Kohderyhmä:**\n{biz['target_audience']}")
                    st.progress(min(row['score']/500, 1.0), text=f"Pöhinäindeksi: {row['score']}")
    else:
        st.error("Yhteysvirhe. Yritä uudelleen.")

st.sidebar.divider()
st.sidebar.info("Tämä työkalu on suunniteltu löytämään matalan kynnyksen automaatiopalveluita.")