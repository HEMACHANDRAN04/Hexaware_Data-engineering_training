emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]

count={}

for email in emails:
    domain=email.split('@')[1]
    if domain in count:
        count[domain]+=1
    else:
        count[domain]=1
print(count)