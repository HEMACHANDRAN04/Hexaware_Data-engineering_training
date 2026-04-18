sentence = "python is easy and python is powerful"

words= sentence.split()
count={}
for w in words:
    if w not in count:
        count[w]=1
    else:
        count[w]+=1
print(count)