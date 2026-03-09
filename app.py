import streamlit as st
from ui.styles import apply_launch_theme
from ui.components import show_newsletter_signup
from core.engine import get_innovation_stream
from core.agent.py import process_commercial_intent # Huom: Jos teet alikansioita, käytä pisteitä

# Alustetaan sovellus
apply_launch_theme()

st.title("AALTO-VUO | INTELLIGENCE")
st.caption("Etsitään nousevat markkinat ja kaupalliset signaalit.")

# Sivupalkki
st.sidebar.title("VALIKKO")
if st.sidebar.button("PÄIVITÄ NÄKYMÄ", use_container_width=True):
    st.rerun()

show_newsletter_signup()

# Päänäkymä
data = get_innovation_stream(15)

if not data.empty:
    for _, row in data.iterrows():
        analysis = process_commercial_intent(row['title'])
        
        # Luodaan kortti
        with st.container():
            st.markdown(f"""
            <div class="opportunity-card">
                <span style="color: #d4af37; font-size: 0.8rem; font-weight: bold;">{analysis['tag'].upper()}</span>
                <h3 style="margin-top: 5px;">{row['title']}</h3>
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
    st.info("Valmistellaan yhteyttä tietolähteisiin...")