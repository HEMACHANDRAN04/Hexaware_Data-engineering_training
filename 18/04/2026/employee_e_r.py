import csv

with open("employee.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# 1. Names
for e in employees:
    print(e["name"])

# 2. IT employees
print("IT employees:")
for e in employees:
    if e["department"] == "IT":
        print(e["name"])

# 3. Average salary
avg = sum(int(e["salary"]) for e in employees) / len(employees)
print("Average salary:", avg)

# 4. Highest salary
top = max(employees, key=lambda x: int(x["salary"]))
print("Highest salary employee:", top["name"])

# 5. Count per department
dept_count = {}
for e in employees:
    dept = e["department"]
    dept_count[dept] = dept_count.get(dept, 0) + 1

print(dept_count)