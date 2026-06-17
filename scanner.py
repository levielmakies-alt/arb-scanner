import requests

markets = requests.get(
    "https://gamma-api.polymarket.com/markets?limit=100",
    timeout=20
).json()

for m in markets:
    question = m.get("question", "")
    if "bitcoin" in question.lower():
        print(question)
        print("Price:", m.get("lastTradePrice"))
        print("---")