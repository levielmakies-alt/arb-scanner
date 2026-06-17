import requests

print("Scanning Polymarket...")

try:
    r = requests.get(
        "https://gamma-api.polymarket.com/markets",
        timeout=20
    )

    print("Status:", r.status_code)

    if r.status_code == 200:
        markets = r.json()
        print("Markets found:", len(markets))

        if len(markets) > 0:
            requests.get(
                "https://api.telegram.org/bot8667226754:AAFINvhhbBmzqMy5hZgRv3SrG58coiBC6Bk/sendMessage",
                params={
                    "chat_id": "999772135",
                    "text": f"Scanner alive. Found {len(markets)} markets."
                }
            )

except Exception as e:
    print("Error:", e)