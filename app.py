import streamlit as st
from ui.styles import apply_launch_theme
from core.engine import get_market_signals
from core.agent import analyze_trade

apply_launch_theme()

st.title("AALTO-VUO | TRADING TERMINAL")
st.write("### real-time market signals . v4.0")

# Sivupalkki
with st.sidebar:
    st.write("---")
    if st.button("REFRESH SIGNALS"):
        st.cache_data.clear()
        st.rerun()
    st.caption("Data: CryptoPanic & Binance Live")

# Datan haku
data = get_market_signals()

if not data.empty:
    for _, row in data.iterrows():
        trade = analyze_trade(row['title'], row['sentiment'], row['price'])
        
        # Tyylikäs kaupankäyntikortti
        st.markdown(f"""
            <div class="card">
                <div style="display: flex; justify-content: space-between;">
                    <span style="color: #d4af37; font-weight: 700;">{row['coin']} / USDT</span>
                    <span style="color: {'#00ff00' if trade['call'] == 'HOT BUY' else '#ff4b4b'}; font-weight: 900;">{trade['call']}</span>
                </div>
                <h2 style="margin: 10px 0; font-size: 1.2rem;">{row['title']}</h2>
                <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 5px; margin: 10px 0;">
                    <p style="margin: 0; font-size: 0.85rem; color: #a0a0a0;"><b>ANALYSIS:</b> {trade['logic']}</p>
                    <p style="margin: 0; font-size: 0.85rem; color: #d4af37;"><b>LIVE PRICE:</b> ${row['price']}</p>
                </div>
                <p style="font-size: 0.7rem; color: #888;">RISK LEVEL: {trade['risk']} | SOURCE: {row['source']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("VIEW CHART", f"https://www.tradingview.com/symbols/{row['coin']}USDT/")
        with c2:
            st.link_button("TRADE NOW", f"https://www.binance.com/en/trade/{row['coin']}_USDT", type="primary")
else:
    st.info("Odotetaan markkinasignaaleja...")