text="I love python coding and i am fond of it"
text=text.lower()
vowels="aeiou"

d={}
for ch in text:
    if ch in vowels:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
print(d)