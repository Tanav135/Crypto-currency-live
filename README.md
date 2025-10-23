# 🪙 CryptoHeatMap — Live Cryptocurrency Trend Dashboard

**CryptoHeatMap** is a real-time cryptocurrency visualization dashboard built using **Streamlit** and the **CoinGecko API**.  
It displays live price trends for major digital currencies with auto-refresh every 10 minutes, helping you track bullish and bearish movements visually.

---

## 📁 Folder Structure
##### CryptoHeatMap/
##### │
##### ├── app.py # Main Streamlit dashboard app
##### │
##### ├── modules/ # Helper Python modules
##### │ ├── api_client.py # Handles CoinGecko API requests (price, history, etc.)
##### │ ├── utils.py # Utility helpers (optional)
##### │
##### ├── data/ # Optional folder for caching/exported data
##### │
##### ├── venv/ # Python virtual environment (ignored by Git)
##### │
##### ├── test_api.py # Test file to check basic CoinGecko API connectivity
##### ├── test_stream.py # Test file for simulated live price streaming
##### ├── test_historical.py # Test file for fetching 7/30-day historical data
##### │
##### ├── requirements.txt # Dependencies list
##### ├── .env # (Optional) Environment variables file
##### ├── .gitignore # Ignore virtual env, cache, and unnecessary files
##### └── README.md # This documentation file

## Steps to run:

### 1)navigate to the folder in cmd
### 2)activate virtual environment( venv\Scripts\activate )
### 3)"streamlit run app.py" in cmd
