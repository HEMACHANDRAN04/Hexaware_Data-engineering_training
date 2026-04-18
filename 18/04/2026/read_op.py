# with open("data.txt","r") as file:
#     for line in file:
#         print(line.strip())
#
# with open("data.txt","r")as  file:
#     students=file.readlines()
# print("Total students:",len(students))

# total=0
# with open("data.txt","r") as file:
#     for line in file:
#         total+=int(line.strip())
# print("Total",total)

# with open("data.txt","w") as file:
#     file.write("Ranjith\n")
#     file.write("basil\n")
#     file.write("Rani\n")
#
# with open("data.txt","a") as file:
#     file.write("priya\n")

languages=["Python\n","Java\n","C++\n"]
with open("data.txt","w") as file:
    file.writelines(languages)