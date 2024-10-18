#write a program that check if a number is prime or not 

num =int(input("enter a number: "))
if num==1:
    print("not a prime number")
if num>1:
    for n in range(2,num):
        if num%2==0:
            print(num, "is not a prime number ")
            break
        else:
            print(num, "num is a prime number")