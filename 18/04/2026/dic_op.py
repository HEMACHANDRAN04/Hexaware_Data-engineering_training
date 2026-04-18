student={
    "name":"Raghavan",
    "age":23,
    "Course":"Python"
}
print(student)
print(student["name"])
print(student["age"])

print(student.get("name"))
print(student.get("Course"))

student["city"]="Hyderabad"
print(student)
