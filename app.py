import streamlit as st
from ui.styles import apply_launch_theme
from core.engine import get_innovation_stream
from core.agent import process_commercial_intent

# 1. Alustus
apply_launch_theme()

st.title("AALTO-VUO")
st.write("### intelligence terminal . v3.0")

# 2. Sivupalkki
with st.sidebar:
    st.write("---")
    if st.button("RESCAN NETWORK"):
        st.cache_data.clear()
        st.rerun()

# 3. Data-analyysi (haetaan 3 parasta)
try:
    data = get_innovation_stream(3)
    
    if not data.empty:
        for _, row in data.iterrows():
            # Haetaan agentin analyysi
            analysis = process_commercial_intent(row['title'])
            
            # Kortin renderöinti
            st.markdown(f"""
                <div class="card">
                    <p style="color: #d4af37; font-size: 0.7rem; font-weight: 700; letter-spacing: 1px;">{analysis['type']}</p>
                    <h2 style="margin: 5px 0 15px 0; font-size: 1.4rem; color: #ffffff;">{row['title']}</h2>
                    <p style="color: #a0a0a0; font-size: 0.95rem; line-height: 1.5;">{analysis['verdict']}</p>
                    <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.05); margin: 20px 0;">
                    <p style="font-size: 0.8rem; color: #d4af37;">POTENTIAL: <b>{analysis['value']}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            # Toiminnot
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("SOURCE CODE", row['url'], use_container_width=True)
            with c2:
                st.link_button("MARKET DATA", analysis['link'], use_container_width=True)
    else:
        st.info("Searching for signals...")

except Exception as e:
    st.error(f"System Error: {e}")