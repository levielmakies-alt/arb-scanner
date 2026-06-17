import requests

poly = requests.get(
    "https://gamma-api.polymarket.com/markets?limit=100",
    timeout=20
).json()

print("Markets loaded:", len(poly))

for market in poly[:20]:
    print(market.get("question", ""))