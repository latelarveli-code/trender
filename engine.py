import requests
import pandas as pd

def fetch_innovation_data(limit=15):
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        ids = requests.get(url, timeout=10).json()[:limit]
        results = []
        for i in ids:
            item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json").json()
            if item and 'title' in item:
                results.append({
                    "title": item['title'],
                    "url": item.get('url', f"https://news.ycombinator.com/item?id={i}"),
                    "score": item.get('score', 0)
                })
        return pd.DataFrame(results)
    except:
        return pd.DataFrame()