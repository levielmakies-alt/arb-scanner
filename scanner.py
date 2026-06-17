import requests

poly = requests.get(
    "https://gamma-api.polymarket.com/markets?limit=500",
    timeout=20
).json()

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()["events"]

keywords = ["pope", "openai", "anthropic", "trump", "taiwan", "china", "bitcoin", "mars"]

matches = []

for p in poly:
    pq = p.get("question", "")
    price = p.get("lastTradePrice")

    for k in kalshi:
        kt = k.get("title", "")

        for word in keywords:
            if word in pq.lower() and word in kt.lower():
                matches.append(f"Possible match:\nPolymarket: {pq}\nPoly price: {price}\nKalshi: {kt}\nKalshi ticker: {k.get('event_ticker')}")
                break

if matches:
    print("\n\n---\n\n".join(matches[:5]))
else:
    print("No possible matches found.")