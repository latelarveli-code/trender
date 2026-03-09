import streamlit as st

# HUOM: Tuonnit alikansioista ilman .py -päätettä!
from ui.styles import apply_launch_theme
from ui.components import show_newsletter_signup
from core.engine import get_innovation_stream
from core.agent import process_commercial_intent

# Alustetaan sovellus ja tyylit
apply_launch_theme()

st.title("AALTO-VUO | INTELLIGENCE")
st.caption("Etsitään nousevat markkinat ja kaupalliset signaalit.")

# Sivupalkin komponentit
show_newsletter_signup()

if st.sidebar.button("PÄIVITÄ NÄKYMÄ", use_container_width=True):
    st.rerun()

# Haetaan ja käsitellään data
data = get_innovation_stream(15)

if not data.empty:
    for _, row in data.iterrows():
        # Analysoidaan jokainen otsikko agentilla
        analysis = process_commercial_intent(row['title'])
        
        # Luodaan visuaalinen kortti (Opportunity Card)
        with st.container():
            st.markdown(f"""
            <div class="opportunity-card">
                <span style="color: #d4af37; font-size: 0.8rem; font-weight: bold;">{analysis['tag'].upper()}</span>
                <h3 style="margin-top: 5px; color: #ffffff;">{row['title']}</h3>
                <p style="font-size: 0.9rem; color: #8b949e;">{analysis['advice']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                st.link_button("LUE LÄHDE", row['url'], use_container_width=True)
            with c2:
                st.link_button(analysis['cta_text'], analysis['affiliate_url'], type="primary", use_container_width=True)
            with c3:
                st.metric("PÖHINÄ", row['score'])
else:
    st.info("Valmistellaan yhteyttä tietolähteisiin... Paina 'Päivitä näkymä' jos data ei lataudu automaattisesti.")