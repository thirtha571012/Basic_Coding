
#character
s="programming"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
seen={}
for ch in s:
    if d[ch]>1:
            if ch not in seen:
                seen[ch]=1
                print(f"{ch}:{d[ch]}")

#words
text=input("enter a string")
words=text.lower().split()
d={}
for word in words:
     d[word]=d.get(word,0)+1
seen={}
for word in words:
    if d[word]>1:
            if word not in seen:
                seen[word]=1
                print(f"{word}:{d[word]}")
