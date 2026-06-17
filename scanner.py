import requests

poly = requests.get(
    "https://gamma-api.polymarket.com/markets",
    timeout=20
).json()

kalshi = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/events",
    timeout=20
).json()

print("=== POLYMARKET ===")

for market in poly[:5]:
    print(market.get("question", "NO QUESTION"))

print("\n=== KALSHI ===")

for event in kalshi["events"][:5]:
    print(event.get("title", "NO TITLE"))