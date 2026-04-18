num=[10,20,30]
num.insert(2,40)
print(num)
num.insert(0,100)
print(num)

num=[10,20,30,40,50]
num.remove(10)
print(num)

num.pop()
print(num)
print(len(num))

numbers=[1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)

fruits=["apple","banana","orange"]
if "apple" in fruits:
    print("apple exists")



numbers=[1,2,3,4,5,6,7,8,9,10]

print(numbers[1:9])

num=[10,20,30,40,50]
num.reverse()
print(num)

num.sort()
print(num)

print(max(num))
print(min(num))
print(sum(num))