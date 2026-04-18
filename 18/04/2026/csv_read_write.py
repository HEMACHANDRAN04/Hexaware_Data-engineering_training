import csv
# with open("data.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
#
# with open("data.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row["name"],row["marks"])

data=[
    ["name","marks"],
    ["priya",88],
    ["karan",75]

]
with open("data.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)