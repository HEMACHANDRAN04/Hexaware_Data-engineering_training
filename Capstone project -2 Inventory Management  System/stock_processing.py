import pandas as pd
import numpy as np

df = pd.read_csv("stock_movements.csv")

print("Original Data")
print(df)

df['quantity'] = df['quantity'].astype(int)

df['movement_date'] = pd.to_datetime(df['movement_date'])

df = df[df['quantity'].notnull()]

stock_summary = df.groupby('product_id')['quantity'].sum()

print("\nCurrent Stock Levels")
print(stock_summary)

reorder_levels = df.groupby('product_id')['reorder_level'].first()

low_stock = stock_summary[stock_summary < reorder_levels]

print("\nLow Stock Products")
print(low_stock)

report = pd.DataFrame({
    'Current_Stock': stock_summary,
    'Reorder_Level': reorder_levels
})

report['Low_Stock_Flag'] = np.where(
    report['Current_Stock'] < report['Reorder_Level'],
    'YES',
    'NO'
)

print("\nFinal Inventory Report")
print(report)

# Save report
report.to_csv("inventory_report.csv")

print("\nReport saved as inventory_report.csv")