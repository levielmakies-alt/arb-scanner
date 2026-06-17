import requests

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()

for event in kalshi["events"][:50]:
    print(event.get("title"))