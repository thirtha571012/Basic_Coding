#character
s="sdfghjkjhgfcdxsdfghjkjhgfdsdfghjkjhgfdsdfghjhgfds"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for ch in s:
    if d[ch]==1:
        print(ch)

#word
text=input("Enter the text")
b=text.lower().split()
d={}
for word in b:
    d[word]=d.get(word,0)+1
for word in b:
    if d[word]==1:
        print(word)