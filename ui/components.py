import streamlit as st
import streamlit.components.v1 as components

def tradingview_chart(symbol):
    # Upotetaan TradingView-widget HTML-komponenttina
    html_code = f"""
    <div class="tradingview-widget-container" style="height:300px;width:100%;">
      <div id="tradingview_chart"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "BINANCE:{symbol}USDT",
        "interval": "H",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_top_toolbar": true,
        "save_image": false,
        "container_id": "tradingview_chart"
      }});
      </script>
    </div>
    """
    components.html(html_code, height=300)