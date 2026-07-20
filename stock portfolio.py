portfolio = {}

def add_stock():
    symbol = input("Enter Stock Symbol: ").upper()
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Purchase Price: "))

    portfolio[symbol] = {
        "quantity": quantity,
        "price": price
    }

    print(f"{symbol} added successfully!\n")


def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.\n")
        return

    total_investment = 0

    print("\nYour Portfolio")
    print("-" * 40)

    for symbol, details in portfolio.items():
        investment = details["quantity"] * details["price"]
        total_investment += investment

        print(f"Stock: {symbol}")
        print(f"Quantity: {details['quantity']}")
        print(f"Purchase Price: ₹{details['price']}")
        print(f"Investment Value: ₹{investment}")
        print("-" * 40)

    print(f"Total Investment: ₹{total_investment}\n")


while True:
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        print("Thank you for using Stock Portfolio Tracker!")
        break
    else:
        print("Invalid choice! Try again.\n")