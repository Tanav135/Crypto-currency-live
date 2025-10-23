# test_api.py
from modules.api_client import CoinGeckoClient
import pprint

def main():
    client = CoinGeckoClient(vs_currency="usd")
    # Test simple price for bitcoin
    print("Fetching simple price for bitcoin...")
    price_json = client.get_simple_price("bitcoin")
    pprint.pprint(price_json)

    # Test market chart (1 day)
    print("\nFetching market chart for bitcoin (1 day, minute interval)...")
    mc = client.get_market_chart("bitcoin", days=1, interval="minute")
    # print how many price points we got and the first example row
    prices = mc.get("prices", [])
    print(f"Returned {len(prices)} price points. Example row (ts_ms, price):")
    if prices:
        pprint.pprint(prices[0])

if __name__ == "__main__":
    main()
