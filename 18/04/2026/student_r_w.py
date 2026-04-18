import json

with open("students.json", "r") as file:
    data=json.load(file)
for s in data["students"]:
    print(s["name"])

print("students in Python Course")
for s in data["students"]:
    if s["course"]=="Python":
        print(s["name"])
top = max(data["students"], key=lambda x: x["marks"])
print("Top student:", top["name"])
students = data["students"]

avg = sum(s["marks"] for s in students) / len(students)
print("Average marks:", avg)

course_count = {}

for s in students:
    course = s["course"]
    course_count[course] = course_count.get(course, 0) + 1

print("Students per course:", course_count)