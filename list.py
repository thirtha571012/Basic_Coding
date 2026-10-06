#list operations
words="Thirtharaj"
words=words.lower()
l=list(words)#you can use list for alphabets and split for words
print(l)
s="".join(l)
print(s)
text="I am learning python programming"
words2=text.split()#it is converted into list of words
print(words2)
sentence=" ".join(words2)#exact opposite of split , does the joining
print(sentence)
print(words.count("a"))
