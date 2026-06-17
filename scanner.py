import requests

KEYWORDS = ["pope", "openai", "anthropic", "bitcoin", "taiwan", "china", "mars", "trump"]

print("=== POLYMARKET ===")
poly = requests.get("https://gamma-api.polymarket.com/markets?limit=500", timeout=20).json()

for word in KEYWORDS:
    print(f"\n--- {word.upper()} ---")
    found = 0
    for m in poly:
        q = m.get("question", "")
        if word in q.lower():
            print(f"{q} | price: {m.get('lastTradePrice')}")
            found += 1
            if found >= 5:
                break

print("\n=== KALSHI ===")
kalshi = requests.get("https://api.elections.kalshi.com/trade-api/v2/events", timeout=20).json()["events"]

for word in KEYWORDS:
    print(f"\n--- {word.upper()} ---")
    found = 0
    for e in kalshi:
        title = e.get("title", "")
        if word in title.lower():
            print(f"{title} | ticker: {e.get('event_ticker')}")
            found += 1
            if found >= 5:
                break