from binance.client import Client
import time

# Your Testnet API keys
API_KEY = "9xfV13tKt31guLDOP0wi5tTCyNbphNdBvSamhFcYgZViGwO43yrJ8ywWawXFAw6z"
API_SECRET = "C8i9ciEcjFl0Kupg16RQy6FSwzFqtPcJtA0gRR4XnJKWyzYb8OxsWi8M5ZKeCGDP"

# Connect to Binance Testnet
client = Client(API_KEY, API_SECRET, testnet=True)

def place_order(symbol, quantity, price):
    try:
        order = client.order_limit_buy(
            symbol=symbol,
            quantity=quantity,
            price=price
        )
        print("Order placed:", order)
    except Exception as e:
        print("Error placing order:", e)

# Example usage
place_order("BTCUSDT", 0.001, 79200)

def fetch_account_balance():
    """Retrieve account balances for all assets."""
    try:
        account = client.get_account()
        for balance in account['balances']:
            print(f"Asset: {balance['asset']}, Free: {balance['free']}, Locked: {balance['locked']}")
    except Exception as e:
        print("Error retrieving account balance:", e)

# Example usage
fetch_account_balance()