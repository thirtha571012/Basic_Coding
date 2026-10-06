#character
s="programming"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)

#words
text=input("Enter the text : ")
words=text.lower().split()
result=[]
for word in words:
    if word not in result:
        result.append(word)
print(result)
print(" ".join(result))