# Stock Portfolio Tracker - CodeAlpha Internship Task (with Pandas)

import pandas as pd

# Step 1: Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 2800,  # Google
    "AMZN": 3300   # Amazon
}

# Step 2: Ask user how many stocks they own
print("Available stocks: AAPL, TSLA, GOOG, AMZN")
portfolio = {}

for stock in stock_prices:
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = qty

# Step 3: Prepare data for DataFrame
data = {
    "Stock": list(portfolio.keys()),
    "Quantity": list(portfolio.values()),
    "Price": [stock_prices[stock] for stock in portfolio.keys()],
    "Total": [portfolio[stock] * stock_prices[stock] for stock in portfolio.keys()]
}

# Step 4: Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Step 5: Print Portfolio Table
print("\n📊 Portfolio Table:\n")
print(df)

# Step 6: Print Total Investment
total_value = df["Total"].sum()
print(f"\n✅ Total Investment Value = ${total_value}")

# Step 7: Save to CSV file
df.to_csv("portfolio_result.csv", index=False)
print("\n📂 Results saved to 'portfolio_result.csv'")
