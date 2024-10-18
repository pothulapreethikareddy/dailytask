#Python Program to check if two Strings are Anagram.

s="preethi"
s1="reddy"
if set(s)==set(s1) and len(s)==len(s1):
    print("anagram")
else:
    print("not")