a="Thirtha"
#normal
for ch in a:
    print(ch)
#without next line
for ch in a:
    print(ch,end="")
print()
#win indexes
for i,ch in enumerate(a):
    print(i,ch)
#finding charcaters
print("t" in a)
print("b" in a)
print("s" not in a)
#finding the position also
print(a.find("T"))
print(a.find("A"))#-1 means not found
##counting characters
print(a.count("h"))
##counting manually
count=0
for ch in a:
    if ch=="a":
        count+=1
print(count)

#counting vowels
vowels="aeiou"
countt=0
a=a.lower()
for ch in a:
    if ch in vowels:
        countt+=1
print(countt)