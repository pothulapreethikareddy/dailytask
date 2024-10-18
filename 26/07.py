# write a program to calculate the factorial of a number by using for loop

n=int(input("enter a number:"))
fact=1
for i in range (1,n+1):
    fact=fact*i 
    print(fact)    