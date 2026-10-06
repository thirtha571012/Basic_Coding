s="hello"
#string indexing
print(s[4])
print(s[-4])

#string slicing

print(s[0:3])
print(s[:3])
print(s[2:]) 
print(s[2:6])
print(s[:])
print(s[0:5:2])
print(s[::2])
print(s[::-1])
print(s[::-2])
print(s[:-1])
#get the first N characters of the string
N = 3
print(s[:N])
#get the last N characters of the string
print(s[-N:])
#odd indexed characters
print(s[1::2])
#even indexed characters
print(s[::2])
#remove the first character from the string
print(s[1:])
#remove the last character from the string
print(s[:-1])
#remove the first and last character from the string
print(s[1:-1])
