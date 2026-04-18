students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}

print("Topper:",max(students))

total=0
for m in students:
    total=total+students[m]
print("AVG:",total/len(students))

print("students above 85:")
for name in students:
    if students[name]>85:
        print("Name:",name)
