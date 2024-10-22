# declaration:
# def
 
def wish(name):
    print("happy Diwali",name)
wish ("Preethi")
 
 
 
def add(s,s1):
    print(s+s1)
    print(s1-s1)
    print(s*s1)
    print(s/s1)
add(40,60)
 
 
def s(x,y):
    print(x+y)
s("preethika","reddy")    
 
 
## by adding marks for students:
 
def marks (maths,physics,english,ED):
   
    total=maths+physics+english+ED
    print(total)
    print((total/totalscore)*100)
 
math=88
physics=78
ED=98
english=95
totalscore=400
marks(math,physics,ED,english)
 
math=88
physics=78
ED=98
english=95
totalscore=400
marks(math,physics,ED,english)
 
 
### return >> it is used to send a value back from a function to where it was called.
 
def add(a,b):
    #print(a+b)
    return a+b
add(20,30)
print(add(20,30))
sum=add(10,20)
print(sum)
 
if sum %2==0:
    print("is even")
else:
    print("not a even")    
 
 
 
##hight frequency element
#
def highest_frequency(l):
    max_count = 0
    most_frequent = None
    for i in l:
        count = l.count(i)
        if count > max_count:
            max_count = count
            most_frequent = i
    return most_frequent
 
s=highest_frequency([1, 3, 5, 2, 6, 2, 7, 2, 8])
print(s)
 