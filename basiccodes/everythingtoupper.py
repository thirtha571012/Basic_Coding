text="i am fond of milk"
#text=text.upper()
#print(text)
#using list for capitalizing
a=text.split()
print(a)
for i in range(len(a)):
    a[i]=a[i].capitalize()
text=" ".join(a)
print(text)