import requests

ticker = "KXNEWPOPE-70"

data = requests.get(
    f"https://api.elections.kalshi.com/trade-api/v2/events/{ticker}",
    timeout=20
).json()

event = data["event"]

print("Title:", event.get("title"))
print("Ticker:", event.get("event_ticker"))

print("Keys:")
for key in event.keys():
    print(key)