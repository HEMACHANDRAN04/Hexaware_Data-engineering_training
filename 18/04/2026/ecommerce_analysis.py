orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]
spend = {}
count = {}

for o in orders:
    c = o["customer"]
    a = o["amount"]

    if c not in spend:
        spend[c] = a
        count[c] = 1
    else:
        spend[c] += a
        count[c] += 1

print(spend)
print(count)

top = ""
max_amt = 0

for c in spend:
    if spend[c] > max_amt:
        max_amt = spend[c]
        top = c

print("Top customer:", top)