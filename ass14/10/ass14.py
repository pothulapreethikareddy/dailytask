### nestlist 
l=[1,2,3,4, [5,6,7, [8,9,10]]]
print(l[4][3][0])
print(l[4][3][2])
print(l[4][3][1])
print(l[2])
print(l[1])
print(l[3])

##alising  >>giving a reference varible name to the existing varibles
##         >> it will give the same id for the varibles
##     >> this means that changes made to one varibles will effect the 
##        other that reference the same the object 
l=["preethi",25,2324]
x=l
print(l)
print(x)
print(id(l))
print(id(x))
l.append(123)
print(l)
print(id(l))
print(id(x))

##cloning  >>to creating of an object or data stucture 
##      >> which means if change made to the clone do not 
# >>>affect original object

l=["preethi",25,2324]
x=l
print(l)
print(x)
x=l[:]
print(id(l))
print(id(x))
l.append("ramadevi")
print(l)
print(id(l))
print(id(x))

###checking the starting and ending of string:

## starting : startswith()
    ## staring of the gmail it should be a word then it will containt the correct 

## ending:  endswith()
## ending of the gmail or web should be (.com)
gmail="preethi@gmail.com"
web="http//youtude.com"
if gmail.startswith("bhupendra"):
    print("the gmail with name")
else:
    print("not")
if web.endswith("com"):
    print("every web page will ends with com")
else:
    print("not") 


    ## comparing of two list:  
l=["preethi","prasad"]
l1=["reddy","ramdevi"]
print(l+l1)   

## ordering of list:
## sort()
s=(1,2,37,6,5,8,4,9)
s1=sorted(s)
print(s1)

## reverse() it will reverse the hole string in list
l=["preethi","ramadevi"]
l.reverse()
print(l)
## reverse by using sciling 
l=["preethi","ramadevi"]
print(l[::-1])

## indexing:
##when we have the more elements in string or a list
## by using index() we can the index value of the speci postion 
l=[1,2,3,4,5,6,7,8,9]
print(l.index(7))
print(l[::-1])
