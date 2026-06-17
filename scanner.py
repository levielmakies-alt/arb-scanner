import requests

ticker = "KXNEWPOPE-70"

r = requests.get(
    f"https://api.elections.kalshi.com/trade-api/v2/events/{ticker}",
    timeout=20
)

print(r.status_code)
print(r.text[:1500])