import requests

poly = requests.get(
    "https://gamma-api.polymarket.com/markets?limit=500",
    timeout=20
).json()

keywords = ["Mars", "Pope", "Taiwan", "Bitcoin", "Trump"]

for market in poly:
    question = market.get("question", "")

    for word in keywords:
        if word.lower() in question.lower():
            print(question)
            break