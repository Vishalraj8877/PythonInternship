import requests
from tabulate import tabulate

# Replace with your real API key from https://www.alphavantage.co/
API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
API_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def get_stock_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except (KeyError, ValueError):
        print(f"Error retrieving data for {symbol}.")
        return None

def add_stock(symbol, quantity):
    symbol = symbol.upper()
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
    else:
        print("Stock not found in portfolio.")

def show_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
        return

    table = []
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            value = price * quantity
            total_value += value
            table.append([symbol, quantity, f"${price:.2f}", f"${value:.2f}"])
    
    print("\nYour Portfolio:")
    print(tabulate(table, headers=["Symbol", "Quantity", "Price", "Value"]))
    print(f"Total Portfolio Value: ${total_value:.2f}")

def menu():
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            remove_stock(symbol)
        elif choice == '3':
            show_portfolio()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()
