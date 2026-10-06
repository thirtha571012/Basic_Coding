s="programming"
d={}
vowels="aeiou"
count=0
for ch in s:
    if ch in vowels:
        d[ch]=d.get(ch,0)+1
        count+=1
print(d)
print(count)