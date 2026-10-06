s="hellooooooooooooooaaaappppuuuyyyttrrrcchjkkgdetruombsdtyulbrtyuibgj"
b={}
for ch in s:
    if ch in b:
        b[ch]+=1
    else:
        b[ch]=1
print(b)