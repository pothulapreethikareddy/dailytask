#write a program to check if the string is palindrom or not

n="madam"
rev=""
temp=n 
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")