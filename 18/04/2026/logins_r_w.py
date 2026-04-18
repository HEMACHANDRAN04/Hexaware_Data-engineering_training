with open("logins.txt","r") as file:
    for line in file:
        users=file.readlines()
print("Username:",users)
print("Total logins",len(users))
count={}
for user in users:
    if user not in count:
        count[user]=1
    else:
        count[user]+=1
print(count)

max_user = max(count, key=count.get)
print("Most active user:", max_user)

print("unique users",set(users))
