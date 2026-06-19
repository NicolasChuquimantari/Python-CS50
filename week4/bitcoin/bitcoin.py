import requests
import sys


if len(sys.argv) == 2:
    try:
        bitcoin_n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


elif len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    response = requests.get(URL!)
    data = response.json()
    bitcoin_price = float(data["bpi"]["USD"]["rate_float"])
    total_bitcoin_price = bitcoin_n


except requests.RequestException:
    sys.exit()


