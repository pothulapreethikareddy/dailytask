#Python Program to count occurrence of a given characters in string.

s="Preethikareddy"
char="d"
c=0
for i in s:
    if i==char:
        c+=1 
print(c)