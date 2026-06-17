ticker = "KXNEWPOPE-70"

r = requests.get(
    f"https://api.elections.kalshi.com/trade-api/v2/markets/{ticker}"
)

print(r.status_code)
print(r.text)