#Membership Operators:
#Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."

l=[1,2,3,4,5,6,7]
if 5 in l:
    print("true")
else:
    print("flase")
postion=0
if 5 in l:
    postion=l.index(5)
    print(postion)
else:
    print("element not found")  
 
#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.

ll=["preethikareddy","keerthireddy","john","sara"]
if "john" in l:
    print("true")
else:
    print("flase")
 
if "sara" in l:
    print("true")
else:
    print("flase")  
 