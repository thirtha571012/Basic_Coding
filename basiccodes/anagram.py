s1="silent"
s2="listen"
d1={}
d2={}
for ch in s1:
    d1[ch]=d1.get(ch,0)+1
for ch in s2:
    d2[ch]=d2.get(ch,0)+1
if d1==d2:
    print(f"{s1} & {s2} are anagrams")