#REPLACE THE FIRST O WITH A

text="helloooooo"
a=list(text)
count=0
for ch in a:
    if ch=="o":
        count+=1
    if count==1:
        a[a.index(ch)] = "a"
text="".join(a)
print(text)
