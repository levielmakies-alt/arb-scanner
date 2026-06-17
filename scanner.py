import requests

url = "https://api.elections.kalshi.com/trade-api/v2/events/KXNEWPOPE-70"

data = requests.get(url, timeout=20).json()
event = data["event"]

print("Title:", event.get("title"))
print("Ticker:", event.get("event_ticker"))
print("Available fields:")

for key in event.keys():
    print(key)