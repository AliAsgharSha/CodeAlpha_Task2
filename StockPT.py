import requests

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'


def get_stock_data(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'Global Quote' in data:
        stock_info = data['Global Quote']
        return {
            'symbol': stock_info['01. symbol'],
            'price': stock_info['05. price'],
            'change': stock_info['09. change'],
            'percent_change': stock_info['10. change percent'],
        }
    else:
        return None


def main():
    portfolio = {}

    while True:
        print("\nStock Portfolio Tracking Tool")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Remove Stock")
        print("4. Track Portfolio Performance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))

            stock_data = get_stock_data(symbol)
            if stock_data:
                portfolio[symbol] = {'quantity': quantity, 'data': stock_data}
                print(f"Added {quantity} shares of {symbol} to your portfolio.")
            else:
                print("Invalid stock symbol or API error. Please try again.")

        elif choice == '2':
            print("\nYour Portfolio:")
            if portfolio:
                for symbol, data in portfolio.items():
                    print(f"{symbol}: {data['quantity']} shares")
                    print(
                        f"Price: ${data['data']['price']} Change: {data['data']['change']} ({data['data']['percent_change']})")
            else:
                print("Your portfolio is empty.")

        elif choice == '3':
            symbol = input("Enter stock symbol to remove: ").upper()
            if symbol in portfolio:
                del portfolio[symbol]
                print(f"{symbol} removed from your portfolio.")
            else:
                print("Stock not found in your portfolio.")

        elif choice == '4':
            total_value = 0
            if portfolio:
                print("\nTracking Portfolio Performance:")
                for symbol, data in portfolio.items():
                    price = float(data['data']['price'])
                    quantity = data['quantity']
                    total_value += price * quantity
                print(f"Total portfolio value: ${total_value:.2f}")
            else:
                print("Your portfolio is empty.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
