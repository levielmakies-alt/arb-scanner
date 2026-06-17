import requests

print("Testing Polymarket + Kalshi APIs...")

try:
    poly = requests.get(
        "https://gamma-api.polymarket.com/markets",
        timeout=20
    )

    print("Polymarket status:", poly.status_code)

    kalshi = requests.get(
        "https://api.elections.kalshi.com/trade-api/v2/events",
        timeout=20
    )

    print("Kalshi status:", kalshi.status_code)

except Exception as e:
    print("Error:", e)