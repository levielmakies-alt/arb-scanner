import requests

print("Arbitrage scanner started")

try:
    r = requests.get("https://gamma-api.polymarket.com/markets")
    print("Polymarket status:", r.status_code)

    if r.status_code == 200:
        markets = r.json()
        print("Markets found:", len(markets))
    else:
        print("Failed to fetch markets")

except Exception as e:
    print("Error:", e)