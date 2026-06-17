import requests

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()

for event in kalshi["events"]:
    title = event.get("title", "")
    if "pope" in title.lower():
        print(title)
        print("Ticker:", event.get("event_ticker"))
        print("---")