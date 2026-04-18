with open("numbers.txt","r") as file:
    numbers=[]
    total=0
    for line in file:
        numbers.append(int(line.strip()))
        total=total+int(line)
print(numbers)
print(total)
print("maximum number: ",max(numbers))
print("minimum number: ",min(numbers))
for num in numbers:
    if num>50:
        print(num)
