import streamlit as st
from ui.styles import apply_launch_theme
from core.engine import get_innovation_stream
from core.agent import process_commercial_intent

apply_launch_theme()

st.title("AALTO-VUO")
st.write("### intelligence terminal . v3.0")

# Sivupalkki minimalistisena
with st.sidebar:
    st.write("---")
    if st.button("SCAN NETWORK"):
        st.rerun()

# Datan haku (vain 3 parasta)
data = get_innovation_stream(3)

if not data.empty:
    for _, row in data.iterrows():
        analysis = process_commercial_intent(row['title'])
        
        # Rakennetaan kortti HTML:llä, jotta se näyttää hyvältä
        st.markdown(f"""
            <div class="card">
                <p style="color: #d4af37; font-size: 0.8rem; font-weight: 500;">{analysis['type']}</p>
                <h2 style="margin-top: 0; margin-bottom: 10px;">{row['title']}</h2>
                <p style="color: #8b949e; font-size: 1rem; line-height: 1.6;">{analysis['verdict']}</p>
                <div style="display: flex; gap: 20px; align-items: center; margin-top: 20px;">
                    <span style="font-weight: bold; color: #d4af37;">POTENTIAL: {analysis['value']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Napit Streamlit-muodossa kortin sisään
        c1, c2 = st.columns([1, 2])
        with c1:
            st.link_button("OPEN SOURCE", row['url'], use_container_width=True)
        with c2:
            st.link_button("ANALYZE MARKET", analysis['link'], use_container_width=True)
else:
    st.write("Initializing secure connection...")