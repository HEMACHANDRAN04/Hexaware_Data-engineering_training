numbers={10,20,30,40}
print(numbers)

num={10,20,30,40,40,30,20}
print(num)

n=[10,20,30,40,40,30,20,10,50]
unique=set(n)
print(unique)

age={10,20,30}
age.add(100)
print(age)

number={10,20}
number.update([30,40,50])
print(number)

set1={10,20,30}
set2={30,40,50}

result=set1.union(set2)
print(result)

result2=set1.difference(set2)
print(result2)

result3=set1.intersection(set2)
print(result3)