import requests
import pandas as pd

def get_innovation_stream(limit=20):
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        ids = requests.get(url, timeout=5).json()[:limit]
        stream = []
        for i in ids:
            item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", timeout=5).json()
            if item and 'title' in item:
                stream.append({
                    "title": item['title'],
                    "url": item.get('url', f"https://news.ycombinator.com/item?id={i}"),
                    "score": item.get('score', 0),
                    "id": i
                })
        return pd.DataFrame(stream)
    except Exception as e:
        return pd.DataFrame()