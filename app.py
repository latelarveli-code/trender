import streamlit as st
from ui.styles import apply_launch_theme
from ui.components import tradingview_chart
from core.engine import get_market_signals, get_fear_and_greed
from core.agent import analyze_trade

apply_launch_theme()

st.title("AALTO-VUO | TERMINAL")
st.write("### real-time crypto intelligence . v4.2")

# 1. Fear & Greed Index - Mittari yläreunaan
fng = get_fear_and_greed()
col_fng, col_status = st.columns([2, 1])

with col_fng:
    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border-left: 5px solid #d4af37;">
            <p style="margin:0; font-size: 0.8rem; color: #888;">MARKET SENTIMENT (FEAR & GREED)</p>
            <h3 style="margin:0; color: #d4af37;">{fng['value']} - {fng['value_classification'].upper()}</h3>
        </div>
    """, unsafe_allow_html=True)

# 2. Sivupalkki
with st.sidebar:
    st.write("---")
    if st.button("FORCE RESCAN", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    st.info("Tip: Get a free API key at CryptoPanic to avoid 'Offline' status.")

# 3. Signaalit
data = get_market_signals()

if not data.empty:
    for _, row in data.iterrows():
        trade = analyze_trade(row['title'], row['sentiment'], row['price'])
        
        with st.container():
            st.markdown(f"""
                <div class="card" style="margin-bottom: 0px; border-radius: 15px 15px 0 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #d4af37; font-weight: 700;">{row['coin']} / USDT</span>
                        <span style="color: {'#00ff00' if 'BUY' in trade['call'] else '#ff4b4b'}; font-weight: 900;">{trade['call']}</span>
                    </div>
                    <h3 style="margin: 10px 0; font-size: 1.1rem;">{row['title']}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"ANALYSIS & CHART: {row['coin']}", expanded=False):
                st.write(f"**Agent Verdict:** {trade['logic']}")
                st.write(f"**Risk Level:** {trade['risk']}")
                tradingview_chart(row['coin'])
                
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("SOURCE", row['url'], use_container_width=True)
            with c2:
                st.link_button("TRADE", f"https://www.binance.com/en/trade/{row['coin']}_USDT", type="primary", use_container_width=True)
            st.write("---")
else:
    st.error("⚠️ SIGNALS OFFLINE: API limits reached. Please insert CryptoPanic API Key in engine.py.")
    st.image("https://cryptopanic.com/static/img/logo-dark.png", width=200)