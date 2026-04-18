import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    sales = list(reader)

# 1. Total revenue
total = sum(int(s["quantity"]) * int(s["price"]) for s in sales)
print("Total revenue:", total)

# 2. Quantity per product
qty = {}
for s in sales:
    product = s["product"]
    qty[product] = qty.get(product, 0) + int(s["quantity"])

print(qty)

# 3. Highest sales product
revenue = {}
for s in sales:
    product = s["product"]
    rev = int(s["quantity"]) * int(s["price"])
    revenue[product] = revenue.get(product, 0) + rev

top = max(revenue, key=revenue.get)
print("Top product:", top)

# 4. Revenue per product
print("Revenue per product:", revenue)

# 5. Products with revenue > 50000
for p in revenue:
    if revenue[p] > 50000:
        print(p)

summary = {}

for s in sales:
    product = s["product"]
    q = int(s["quantity"])
    r = q * int(s["price"])

    if product not in summary:
        summary[product] = {"qty": 0, "revenue": 0}

    summary[product]["qty"] += q
    summary[product]["revenue"] += r

print("Product Sales Summary")
for p in summary:
    print(f"{p} → Qty: {summary[p]['qty']} Revenue: {summary[p]['revenue']}")