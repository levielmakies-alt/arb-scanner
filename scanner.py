import requests

url = "https://api.elections.kalshi.com/trade-api/v2/events/KXNEWPOPE-70"

r = requests.get(url, timeout=20)

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("content-type"))
print("Body:")
print(r.text[:2000])