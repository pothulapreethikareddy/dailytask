#Advanced Challenges:
#Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
#Another containing only the odd numbers.
l=[l for l in range (1,25+1)]
print(l)
even_num=[]
odd_num=[]
for i in l:
    if(i%2==0):
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)       
#Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
l=[1,2,3,1,3,5,4,3,6,7,5,4]
print(set(l))

#Given a list of tuples representing (name, age), sort the list by age in ascending order.

t=[("preethi",55),("keerthi",45)]
t.sort()
print(t)