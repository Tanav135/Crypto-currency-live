from modules.api_client import CoinGeckoClient

client = CoinGeckoClient()
data = client.get_historical_data("bitcoin", "usd", 30)

print(f"Fetched {len(data)} data points for Bitcoin (last 30 days):")
for entry in data:
    print(entry)
