import requests
import sys

def check_args():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

try:
    check_args()

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = response.json()["bpi"]["USD"]["rate_float"]
    per_coin = rate * float(sys.argv[1])

    print(f"${per_coin:,.4f}")

except requests.RequestException:
    sys.exit()
