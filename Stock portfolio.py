# Stock Portfolio Tracker
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(stock, "- $", stock_prices[stock])

print("\nEnter the stocks you want to buy.")
print("Type 'done' when you are finished.")

while True:
    stock = input("\nEnter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = quantity

print("\n====================================")
print("          PORTFOLIO SUMMARY")
print("====================================")

for stock in portfolio:
    price = stock_prices[stock]
    quantity = portfolio[stock]
    investment = price * quantity

    total_investment += investment

    print(stock)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Investment: $", investment)
    print("------------------------------------")

print("Total Investment: $", total_investment)


with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("========================\n")

    for stock in portfolio:
        price = stock_prices[stock]
        quantity = portfolio[stock]
        investment = price * quantity

        file.write(
            f"{stock} - Quantity: {quantity}, "
            f"Price: ${price}, Investment: ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\n Portfolio saved to portfolio.txt")
