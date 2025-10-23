import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import plotly.express as px
from modules.api_client import CoinGeckoClient
from modules.utils import format_price_data

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="CryptoHeatMap Dashboard",
    layout="wide",
    page_icon="💹",
)

st.title("💹 CryptoHeatMap — 30-Day Multi-Coin Dashboard")
st.markdown("Compare 30-day trends of your favorite cryptocurrencies. Data auto-refreshes every 10 minutes.")

# ----------------------------
# AUTO-REFRESH EVERY 10 MIN
# ----------------------------
# (10 minutes = 600 seconds)
count = st_autorefresh(interval=10 * 60 * 1000, limit=None, key="crypto_refresh")
st.caption(f"⏱️ Auto-refresh count: {count} (every 10 minutes)")

# ----------------------------
# FETCH & CACHE DATA
# ----------------------------
@st.cache_data(ttl=600)  # cache expires every 10 minutes
def fetch_coin_data(coins):
    client = CoinGeckoClient()
    data_dict = {}
    for coin in coins:
        try:
            raw_data = client.get_historical_data(coin, "usd", 30)
            df = format_price_data(raw_data, coin)
            data_dict[coin] = df
        except Exception as e:
            st.error(f"Error fetching {coin}: {e}")
    return data_dict

# ----------------------------
# USER SELECTION
# ----------------------------
available_coins = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano", "bnb"]
selected_coins = st.multiselect(
    "Select cryptocurrencies to compare (max 4 recommended):",
    available_coins,
    default=["bitcoin", "ethereum", "solana", "dogecoin"]
)

# ----------------------------
# DISPLAY SEPARATE CHARTS
# ----------------------------
if selected_coins:
    data_dict = fetch_coin_data(selected_coins)

    st.subheader("📊 30-Day Price Trends")
    cols = st.columns(2)  # 2 charts per row

    for i, coin in enumerate(selected_coins):
        df = data_dict[coin]
        fig = px.line(
            df,
            x="date",
            y="price",
            title=f"{coin.capitalize()} — 30-Day Trend",
            line_shape="spline",
            markers=True,
        )
        fig.update_traces(line=dict(width=3))
        fig.update_layout(
            template="plotly_dark",
            hovermode="x unified",
            height=400,
            xaxis_title="Date",
            yaxis_title="Price (USD)",
        )

        # Place each chart in one of the two columns
        cols[i % 2].plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # SUMMARY TABLE
    # ----------------------------
    st.subheader("💡 Summary Insights (Last 30 Days)")
    summary = pd.DataFrame({
        "Highest Price (USD)": [data_dict[c]["price"].max() for c in selected_coins],
        "Lowest Price (USD)": [data_dict[c]["price"].min() for c in selected_coins],
        "Average Price (USD)": [data_dict[c]["price"].mean() for c in selected_coins],
    }, index=[c.capitalize() for c in selected_coins])

    st.dataframe(summary.style.format("{:,.2f}"))

else:
    st.warning("Please select at least one cryptocurrency to display.")
