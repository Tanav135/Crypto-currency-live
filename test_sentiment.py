# test_sentiment.py

from modules.sentiment import derive_sentiment_temperature

def main():
    # Simulated price history
    prices = [100, 101, 102, 103, 104]   # upward trend
    result = derive_sentiment_temperature(prices)
    print("Example 1 (Uptrend):", result)

    prices = [100, 100, 100, 100, 100]   # flat
    result = derive_sentiment_temperature(prices)
    print("Example 2 (Stable):", result)

    prices = [104, 103, 102, 101, 100]   # downtrend
    result = derive_sentiment_temperature(prices)
    print("Example 3 (Downtrend):", result)

if __name__ == "__main__":
    main()
