#character
s="dfghjkjhgfdfghjhgfdfghjklkjhgytrexcvbmnbvertjnvdf"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)

#words

text=input("enter a string")
words=text.lower().split()
result=[]
for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))