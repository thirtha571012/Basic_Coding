#most frequent character
s="ppppppppppppppppprrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrooooooooooooogrammmmmmiiiinnnnnnnnnnnngggggg"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
max_char=max(d,key=d.get)
print(f"{max_char} : {d[max_char]}")

#most frequent word
text=input("Enter the string : ")
words=text.lower().split()
d={}
for word in words:
    d[word]=d.get(word,0)+1
print(d)
max_word=max(d,key=d.get)
print(f"{max_word} : {d[max_word]}")
