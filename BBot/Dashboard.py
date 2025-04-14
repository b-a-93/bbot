import streamlit as st
import pandas as pd
from binance.client import Client

# Binance API keys (testnet for testing)
API_KEY = "9xfV13tKt31guLDOP0wi5tTCyNbphNdBvSamhFcYgZViGwO43yrJ8ywWawXFAw6z"
API_SECRET = "C8i9ciEcjFl0Kupg16RQy6FSwzFqtPcJtA0gRR4XnJKWyzYb8OxsWi8M5ZKeCGDP"

# Connect to Binance Testnet
client = Client(API_KEY, API_SECRET, testnet=True)

# Fetch data functions
def get_last_10_orders_with_status(symbol):
    """Fetch the last 10 orders with status for a given trading pair."""
    orders = client.get_all_orders(symbol=symbol)
    # Convert orders to a DataFrame
    df = pd.DataFrame(orders)
    # Select only relevant columns, including 'status'
    df = df[['orderId', 'symbol', 'price', 'origQty', 'executedQty', 'status']]
    return df.tail(10)  # Return the last 10 orders

def get_open_orders(symbol):
    """Fetch open orders."""
    orders = client.get_open_orders(symbol=symbol)
    return pd.DataFrame(orders)

def get_account_assets():
    """Fetch account balances."""
    account = client.get_account()
    balances = pd.DataFrame(account['balances'])
    return balances[balances['free'] != '0.000000']  # Show only non-zero balances

def fetch_current_price(symbol="BTCUSDT"):
    """Fetch the current price of a given trading pair."""
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker['price'])
    except Exception as e:
        print("Error fetching price:", e)
        return None



# Dashboard
st.title("Binance Trading Dashboard")

st.subheader("Current Bitcoin (BTC) Price")
btc_price = fetch_current_price("BTCUSDT")
if btc_price:
    st.metric(label="BTC Price (USDT)", value=f"${btc_price:,.2f}")
else:
    st.error("Unable to fetch BTC price.")

symbol = st.text_input("Enter Symbol (e.g., BTCUSDT):", "BTCUSDT")

if st.button("Refresh Data"):
    # Re-run data fetching logic here
    last_10_orders_with_status = get_last_10_orders_with_status(symbol)
    st.dataframe(last_10_orders_with_status)

# Last 10 Orders
# Update the Streamlit section for 'Last 10 Orders'
st.subheader(f"Last 10 Orders for {symbol} (with Status)")
last_10_orders_with_status = get_last_10_orders_with_status(symbol)
st.dataframe(last_10_orders_with_status)

# Open Orders
st.subheader("Open Orders")
open_orders = get_open_orders(symbol)
st.dataframe(open_orders)

# Account Assets
st.subheader("Account Assets")
assets = get_account_assets()
st.dataframe(assets)

