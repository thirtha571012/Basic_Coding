#REMOVING T FROM THE WORD
text="thirtharaj"
a=list(text)
for ch in a:
    if ch=="t":
        a.remove(ch)
text="".join(a)
print(text)