#Python program to replace the string space with a given character.

s = "python "  
c = " open source program "  
s1 = ""  
for i in s:
    if i == " ":
        s1 += c 
    else:
        s1 += i 
print("string:",s1)