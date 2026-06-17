import requests

poly = requests.get(
    "https://gamma-api.polymarket.com/markets?limit=500",
    timeout=20
).json()

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()["events"]

keywords = [
    "next pope",
    "taiwan",
    "bitcoin",
    "openai",
    "anthropic",
    "mars",
    "china",
]

matches = []

for p in poly:
    pq = p.get("question", "").lower()
    price = p.get("lastTradePrice")

    for k in kalshi:
        kt = k.get("title", "").lower()

        for word in keywords:
            if word in pq and word in kt:
                matches.append(
                    f"Possible match:\n"
                    f"Polymarket: {p.get('question')}\n"
                    f"Poly price: {price}\n"
                    f"Kalshi: {k.get('title')}\n"
                    f"Kalshi ticker: {k.get('event_ticker')}"
                )
                break

if matches:
    print("\n\n---\n\n".join(matches[:10]))
else:
    print("No possible matches found.")