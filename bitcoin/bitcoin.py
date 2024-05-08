import requests
import json
import sys

def main():
    if len(sys.argv)==2:
        try:
            var = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument  ")

    try:

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except requests.RequestException:

        sys.exit("There was an ambiguous exception that occurred while handling your request.")

    except  requests.HTTPError:


        sys.exit("Http Error")


    response=response.json()
    amount = float(var*float(response["bpi"]["USD"]["rate_float"]))
    print(f"${amount:,.4f}")


main()