import requests

def fetch_url(url):
    try:
        r = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        })
        r.raise_for_status()
        return r.text
    except Exception as e:
        return None
