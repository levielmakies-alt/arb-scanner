import requests

print("Loading markets...")

poly = requests.get(
    "https://gamma-api.polymarket.com/markets",
    timeout=20
).json()

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()

print("Polymarket markets:", len(poly))

if "events" in kalshi:
    print("Kalshi events:", len(kalshi["events"]))
else:
    print("Kalshi response:", kalshi)