import json
with open("orders.json","r") as file:
    data = json.load(file)

orders=data["orders"]

for order in orders:
    print(order)
total_revenue=0
for order in orders:
    total_revenue += order["amount"]
print("Total revenue",total_revenue)

spending = {}
for o in orders:
    customer = o["customer"]
    spending[customer] = spending.get(customer, 0) + o["amount"]

print(spending)

top_customer = max(spending, key=spending.get)
print("Top customer:", top_customer)


order_count = {}
for o in orders:
    customer = o["customer"]
    order_count[customer] = order_count.get(customer, 0) + 1

print(order_count)