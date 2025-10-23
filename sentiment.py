# modules/sentiment.py

"""
Sentiment Temperature Module
----------------------------
This module converts recent crypto price data into a "sentiment temperature"
based on short-term price movement.

- Positive % change → Hot (Bullish)
- Negative % change → Cold (Bearish)
- Stable → Neutral

It outputs both:
1. A numeric temperature score (0–100)
2. A qualitative label (Hot, Neutral, Cold)
"""

import numpy as np


def calculate_percentage_change(prices):
    """
    Calculate the short-term percentage change between the first and last price.

    :param prices: (list of float) Recorded prices over time.
    :return: (float) Percentage change.
    """
    if len(prices) < 2:
        return 0.0

    start_price = prices[0]
    end_price = prices[-1]
    if start_price == 0:
        return 0.0

    percent_change = ((end_price - start_price) / start_price) * 100
    return round(percent_change, 3)


def derive_sentiment_temperature(prices):
    """
    Derive the sentiment 'temperature' based on recent price trend.

    :param prices: (list of float) Recent price history
    :return: dict with fields:
             {
                'change_percent': float,
                'temperature_score': int,
                'sentiment_label': str
             }
    """
    change_percent = calculate_percentage_change(prices)

    # Convert % change → temperature scale (0–100)
    # 0°C = very bearish, 100°C = very bullish, 50°C = neutral baseline
    temperature_score = np.clip(50 + change_percent * 10, 0, 100)

    # Assign qualitative label
    if change_percent > 1:
        label = "🔥 Hot (Bullish)"
    elif change_percent < -1:
        label = "🧊 Cold (Bearish)"
    else:
        label = "😐 Neutral"

    return {
        "change_percent": change_percent,
        "temperature_score": round(float(temperature_score), 2),
        "sentiment_label": label
    }
