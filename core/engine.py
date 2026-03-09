import requests
import pandas as pd

def get_market_signals():
    # CryptoPanic API - voit lisätä oman avaimen tähän kohtaan
    # Jos jätät 'auth_token=' tyhjäksi, se toimii rajoitetusti
    api_key = "" 
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}&public=true"
    
    try:
        response = requests.get(url, timeout=10)
        posts = response.json().get('results', [])[:6] # Haetaan 6 kuuminta
        
        signals = []
        for p in posts:
            currencies = p.get('currencies', [])
            coin_code = currencies[0].get('code') if currencies else "BTC"
            
            # Haetaan hinta Binancesta
            try:
                price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin_code}USDT"
                price_data = requests.get(price_url, timeout=2).json()
                price = f"{float(price_data['price']):.2f}" if 'price' in price_data else "N/A"
            except:
                price = "Check Live"

            signals.append({
                "title": p.get('title'),
                "url": p.get('url'),
                "coin": coin_code,
                "price": price,
                "sentiment": p.get('votes', {}).get('positive', 0),
                "source": p.get('domain', 'CryptoNews')
            })
        return pd.DataFrame(signals)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()