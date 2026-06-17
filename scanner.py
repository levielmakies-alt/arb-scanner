import requests

r = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
)

events = r.json()["events"]

for event in events:
    title = event.get("title", "")

    if "pope" in title.lower():
        print(title)
        print("Ticker:", event.get("event_ticker"))

        markets = event.get("markets", [])

        if len(markets) > 0:
            print("Market:", markets[0].get("ticker"))

        print("---")