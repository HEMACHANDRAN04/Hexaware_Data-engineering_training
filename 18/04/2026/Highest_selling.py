sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]

total = {}
for s in sales:
    p = s["product"]
    q = s["qty"]

    if p not in total:
        total[p] = q
    else:
        total[p] += q

print(total)
max_p = ""
max_q = 0

for p in total:
    if total[p] > max_q:
        max_q = total[p]
        max_p = p

print("Highest:", max_p)