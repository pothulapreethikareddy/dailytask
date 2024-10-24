# functions
# arguments are in different types
 
# 1.positional arguments
##  the first argument goes to the first parameter and the second to the second parameter
##  it will the value based on the postion of given arguments
 
def mul(a,b):
    print(a)
    print(b)
    print(a*b)
mul(10,20)
 
def mul(b,a):
    print(a)
    print(b)
    print(b*a)
 
mul(10,20)  

 
def name (name1,name2):
    print(name1)
    print(name2)
    return (name1+name2)
print(name("Preethika","Reddy"))
 
 
def name (name2,name1,name3):
    print(name1)
    print(name2)
    print(name3)
    return (name1+name2+name3)
print(name("Pothula ","Preethika","Reddy"))

 
 
#keyword arguments:
#    >>Keyword arguments lets us to pass values to a function using the parameter names
##  >> paramter="value"
 
def greet(name,msg):
    print(name,msg)
greet(name="Preethika Reddy",msg="wish me on november 5th")
 
 
def greet(msg,name):
    print(name,msg)
greet(name="Preethika Reddy",msg="wish me on november 5th")
 
# because we assigined the parameter to the value so if we change the
## def parameter also no problem
 
 
def add(a,b):
    print(a)
    print(b)
    return (a+b)
print(add(a=40,b=5))
 
def add(b,a):
    print(a)
    print(b)
    return (a+b)
print(add(a=40,b=5))
 
 
## variable lenght arguments:
##   >Variable length arguments allow you to pass a variable number of arguments to a function
 
def factorial(*n):
    f = []
    for i in n:
        if i < 0:
            return i  
        fact = 1
        for i in range(1,i+1):
            fact *= i
            f.append(fact)
    return f
 
print(factorial(1,3,5))
 
 
 
## variable keyword length arguments:
#it will store in the from of dictinary
#Variable keyword arguments allow you to pass a variable number of keyword arguments to a function
# it will store the elemnts in the key value pari
 
def fruits(**l):
    for k,v in l.items():
        print(k,"-",v)
    print(sum(l.values()))
 
fruits(apple=45,pineapple=50,kiwi=30,orange=70,custedapple=60)
 
 
## default arguments:
# Default arguments allow you to specify default values for function parameters
 
 
def append_to(a, l=None):
    if l is None:
        l = []
    l.append(a)  
    return l
l1=[]
print(append_to(1,l1))  
print(append_to(2,l1))  
print(append_to(3,l1))  
print(append_to(4,l1))  
 
 
 