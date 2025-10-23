from modules.api_client import CoinGeckoClient
from modules.utils import format_price_data, combine_coin_data

client = CoinGeckoClient()

# Fetch data for multiple coins
coins = ["bitcoin", "ethereum", "solana", "dogecoin"]
data_dict = {}

for coin in coins:
    raw_data = client.get_historical_data(coin, "usd", 7)
    df = format_price_data(raw_data, coin)
    data_dict[coin] = df

# Combine all into one DataFrame
combined_df = combine_coin_data(data_dict)

print(combined_df.head(10))
