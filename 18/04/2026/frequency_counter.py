numbers = [10,20,10,30,20,10,40]

frequency = {}
for num in numbers:
    if num not in frequency:
        frequency[num]=1
    else:
        frequency[num]=frequency[num]+1
print(frequency)