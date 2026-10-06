s="cat dog horse lion tiger dragon"
s=s.lower()
d={}
for ch in s:
    if ch!=" ":
        d[ch]=d.get(ch,0)+1
print(d)