import pandas as pd
from datetime import datetime

def format_price_data(raw_data, coin_name):
    """
    Convert CoinGecko raw [timestamp, price] list into a pandas DataFrame.
    Adds a readable 'date' column and 'coin' column.
    """
    df = pd.DataFrame(raw_data, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df["coin"] = coin_name
    return df[["date", "coin", "price"]]

def combine_coin_data(data_dict):
    """
    Combine multiple coins' DataFrames into one.
    Example input: {"bitcoin": df1, "ethereum": df2, ...}
    """
    combined_df = pd.concat(data_dict.values(), ignore_index=True)
    return combined_df
