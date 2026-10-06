text=input("Enter a string ")
words=text.lower().split()
d={}
for word in words:
    d[word]=d.get(word,0)+1
for word in d:
    if d[word]>1:
        print(f"{word} : {d[word]}")
result=[]
seen={}
for word in words:
    if word not in seen :
        seen[word]=1
        result.append(word)
print(" ".join(result))