import requests
import pandas as pd

def get_market_signals():
    # CryptoPanic API (Ilmainen versio toimii ilman avaintakin rajoitetusti, 
    # mutta suosittelen hakemaan ilmaisen API-avaimen heiltä)
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=TAALA_ILMAINEN_AVAIN&public=true"
    
    try:
        response = requests.get(url, timeout=10)
        posts = response.json().get('results', [])[:10]
        
        signals = []
        for p in posts:
            coin = p.get('currencies', [None])[0]
            coin_code = coin.get('code') if coin else "BTC"
            
            # Haetaan hinta (ilmainen haku Binance API:sta)
            price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin_code}USDT"
            price_data = requests.get(price_url).json()
            price = price_data.get('price', "N/A")

            signals.append({
                "title": p.get('title'),
                "url": p.get('url'),
                "coin": coin_code,
                "price": price,
                "sentiment": p.get('votes', {}).get('positive', 0),
                "source": p.get('domain')
            })
        return pd.DataFrame(signals)
    except:
        return pd.DataFrame()