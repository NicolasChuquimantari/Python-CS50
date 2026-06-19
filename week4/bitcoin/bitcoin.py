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
    # Get bitcoin price
    bitcoin_price = float(data["bpi"]["USD"]["rate_float"])
    # Calculate total cost
    total_bitcoin_price = bitcoin_n * bitcoin_price
    print(f"${amount:,.4f}")


except requests.RequestException:
    sys.exit()


