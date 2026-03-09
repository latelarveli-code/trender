import streamlit as st
from ui.styles import apply_launch_theme
from ui.components import tradingview_chart
from core.engine import get_market_signals, get_fear_and_greed
from core.agent import analyze_trade

apply_launch_theme()

# Header-osio
st.title("AALTO-VUO | PRO TERMINAL")
fng = get_fear_and_greed()

c1, c2 = st.columns([1, 3])
with c1:
    st.metric("FEAR & GREED", fng['value'], fng['value_classification'])
with c2:
    st.write("### real-time market arbitrage . v4.4")

# Datan haku
data = get_market_signals()

if not data.empty:
    for _, row in data.iterrows():
        # Agentti analysoi äänestystulokset
        trade = analyze_trade(row['title'], row['sentiment'], row['negative'])
        
        with st.container():
            # Tyylitelty kortti
            status_color = "#00ff00" if "BUY" in trade['call'] else "#ff4b4b" if "SELL" in trade['call'] else "#d4af37"
            
            st.markdown(f"""
                <div class="card" style="border-left: 6px solid {status_color};">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: {status_color}; font-weight: 800; font-size: 1.2rem;">{trade['call']}</span>
                        <span style="color: #888; font-size: 0.8rem;">{row['coin']} / USDT @ ${row['price']}</span>
                    </div>
                    <h3 style="margin: 15px 0 5px 0; line-height: 1.2;">{row['title']}</h3>
                    <p style="color: #d4af37; font-size: 0.8rem; margin-bottom: 15px;">SOURCE: {row['source'].upper()}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Toiminnot ja kaavio
            with st.expander("PRO ANALYSIS & LIVE CHART"):
                st.info(f"**Agent Verdict:** {trade['logic']}")
                tradingview_chart(row['coin'])
                
            col_a, col_b = st.columns(2)
            with col_a:
                st.link_button("SOURCE NEWS", row['url'], use_container_width=True)
            with col_b:
                st.link_button("EXECUTE TRADE", f"https://www.binance.com/en/trade/{row['coin']}_USDT", type="primary", use_container_width=True)
            st.write("---")
else:
    st.warning("⚠️ Terminal is scanning... If this persists, verify your API Key in core/engine.py.")

st.sidebar.success("API CONNECTION: ACTIVE")