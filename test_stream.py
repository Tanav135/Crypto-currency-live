# test_stream.py

from modules.api_client import CoinGeckoClient

def main():
    client = CoinGeckoClient()
    client.stream_live_prices("bitcoin", interval=5, duration=30)

if __name__ == "__main__":
    main()
