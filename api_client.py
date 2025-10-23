# modules/api_client.py

"""
CoinGecko API Client Module
---------------------------
This module handles communication with the CoinGecko public API.

Features:
- Fetch live (approx. real-time) crypto prices using /simple/price
- Simulate real-time streaming by polling prices at a fixed interval
- Safe for CoinGecko's free API tier (no key required)
"""

import requests
import time


class CoinGeckoClient:
    """
    A lightweight API client to interact with CoinGecko's public endpoints.
    """

    def __init__(self, base_url="https://api.coingecko.com/api/v3"):
        """
        Initialize the API client.
        :param base_url: CoinGecko base API endpoint
        """
        self.base_url = base_url

    def get_simple_price(self, coin_id="bitcoin", vs_currency="usd"):
        """
        Fetch the current price and 24-hour change for a given cryptocurrency.

        :param coin_id: (str) The coin's ID as per CoinGecko (e.g., 'bitcoin', 'ethereum')
        :param vs_currency: (str) The comparison currency (e.g., 'usd', 'inr')
        :return: (dict) Price data in the form:
                 {
                    'bitcoin': {
                        'usd': 105000,
                        'usd_24h_change': 1.52
                    }
                 }
        """
        url = f"{self.base_url}/simple/price"
        params = {
            "ids": coin_id,
            "vs_currencies": vs_currency,
            "include_24hr_change": "true"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[CoinGecko] API request failed: {e}")
            return None

    def stream_live_prices(self, coin_id="bitcoin", vs_currency="usd", interval=10, duration=60):
        """
        Simulate real-time price streaming by polling CoinGecko's simple price endpoint.

        :param coin_id: (str) The cryptocurrency ID
        :param vs_currency: (str) The currency to compare against (default: USD)
        :param interval: (int) Time gap (in seconds) between each API call
        :param duration: (int) Total streaming duration in seconds
        :return: (list) List of price values recorded over the duration
        """
        prices = []
        print(f"Starting live price stream for {coin_id.upper()} (updates every {interval}s)...")
        start_time = time.time()

        while time.time() - start_time < duration:
            data = self.get_simple_price(coin_id, vs_currency)
            if data:
                price = data[coin_id][vs_currency]
                change = data[coin_id].get(f"{vs_currency}_24h_change", 0)
                prices.append(price)
                print(f"Price: {price:.2f} {vs_currency.upper()} | 24h Change: {change:.2f}%")
            else:
                print("[CoinGecko] Failed to fetch data, retrying next cycle...")

            time.sleep(interval)

        print("Live streaming ended.")
        return prices

    def get_historical_data(self, coin_id="bitcoin", vs_currency="usd", days=30):
        """
        Fetch historical market data (price, market cap, volume) for the past 'days' days.
        Example endpoint: /coins/bitcoin/market_chart?vs_currency=usd&days=7
        """
        url = f"{self.base_url}/coins/{coin_id}/market_chart"
        params = {"vs_currency": vs_currency, "days": days, "interval": "daily"}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

        # Extract only prices: [ [timestamp, price], ... ]
        prices = data["prices"]
        return prices
