import requests
import pandas as pd

def get_fear_and_greed():
    try:
        r = requests.get("https://api.alternative.me/fng/", timeout=5).json()
        return r['data'][0]
    except:
        return {"value": "50", "value_classification": "Neutral"}

def get_market_signals():
    # SIJOITA AVAIMESI TÄHÄN
    api_key = "1d8b5e3e1e4ea7c51e784082488ac85410bdfc54" 
    
    # Haetaan uutiset, jotka sisältävät valuuttatietoa ja positiivista nostetta
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}&kind=news&filter=hot"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return pd.DataFrame()
            
        posts = response.json().get('results', [])[:10]
        
        signals = []
        for p in posts:
            currencies = p.get('currencies', [])
            coin_code = currencies[0].get('code') if currencies else "BTC"
            
            # Haetaan tarkka hinta Binancesta
            try:
                price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin_code}USDT"
                p_resp = requests.get(price_url, timeout=2).json()
                price = f"{float(p_resp['price']):.4f}" if 'price' in p_resp else "N/A"
            except:
                price = "Check"

            signals.append({
                "title": p.get('title'),
                "url": p.get('url'),
                "coin": coin_code,
                "price": price,
                "sentiment": p.get('votes', {}).get('positive', 0),
                "negative": p.get('votes', {}).get('negative', 0),
                "source": p.get('domain', 'CryptoNews')
            })
        return pd.DataFrame(signals)
    except:
        return pd.DataFrame()