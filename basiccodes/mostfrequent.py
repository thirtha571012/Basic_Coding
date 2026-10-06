#character
s="abcdtuoljbvbnmmhjgfdswrtimnvghgjj"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
most_freq=max(d,key=d.get)
print(f"{most_freq} : {d[most_freq]}")

#words
text=input("Enter the text: ")
words=text.lower().split()
d={}
for word in words:
    d[word]=d.get(word,0)+1 #.get returns the count , if not exists then 0
print(d)
most_freq=max(d,key=d.get)
print(f"{most_freq} : {d[most_freq]}")