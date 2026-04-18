inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}

inventory["monitor"]=8
print(inventory)

inventory["laptop"]=10-2
print(inventory)

for item in inventory:
    if inventory[item]<10:
        print(item)