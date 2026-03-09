import streamlit as st
from ui.styles import apply_launch_theme
from ui.components import tradingview_chart
from core.engine import get_market_signals
from core.agent import analyze_trade

# 1. Alustus
apply_launch_theme()

st.title("AALTO-VUO | TERMINAL")
st.write("### real-time crypto intelligence . v4.1")

# 2. Sivupalkki
with st.sidebar:
    st.write("---")
    if st.button("RESCAN MARKETS", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    st.caption("Live Feed: CryptoPanic | Binance | TradingView")

# 3. Markkinasignaalien ajo
data = get_market_signals()

if not data.empty:
    for _, row in data.iterrows():
        # Agentin analyysi (käytetään v4.0 agenttia)
        trade = analyze_trade(row['title'], row['sentiment'], row['price'])
        
        with st.container():
            # Kortin visuaalinen HTML-pohja
            st.markdown(f"""
                <div class="card" style="margin-bottom: 0px; border-bottom: none; border-radius: 15px 15px 0 0;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h2 style="margin: 0; color: #d4af37;">{row['coin']} / USDT</h2>
                        <span style="background: {'#00ff00' if 'BUY' in trade['call'] else '#ff4b4b'}; 
                                     color: black; padding: 2px 10px; border-radius: 5px; font-weight: 900;">
                            {trade['call']}
                        </span>
                    </div>
                    <p style="margin: 10px 0; font-size: 1.1rem; font-weight: 500;">{row['title']}</p>
                    <p style="color: #888; font-size: 0.8rem;">PRICE: ${row['price']} | SENTIMENT: +{row['sentiment']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Upotetaan TradingView-kaavio kortin alle
            with st.expander(f"VIEW LIVE CHART: {row['coin']}", expanded=False):
                tradingview_chart(row['coin'])
                
            # Toiminnot
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("READ SOURCE", row['url'], use_container_width=True)
            with c2:
                st.link_button("EXECUTE ON BINANCE", f"https://www.binance.com/en/trade/{row['coin']}_USDT", type="primary", use_container_width=True)
            st.write("---")
else:
    st.warning("⚠️ Signals offline. API limits or connectivity issues. Try 'Rescan Markets'.")