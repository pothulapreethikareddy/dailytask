#Tuple is a collection that is ordered and immutable it can be allow duplicates.
#tuple can be represented as the round brakets.

t=()
print(type(t))
t=(1,2,3,45,5)
print(t)
print(type(t))

t=tuple("sai")
print(t)

#output
# ('s','a','i')

## we can also give the tuple element with the single element aslo
t=(20)
print(type(t))
 ## we get the int as an output 
 ## so we have to use the comma in the end of the elememt


t=(20,)
print(type(t))
## here we get the ouput as tuple

## we can accesing element from tuple also
## here we can acces the elements by using of index and sciling aslo


t=(1,2,3,4,5,6,7,8,9)
print(t[2])  ## by using indexing
print(t[6])
print(t[3:6]) ## by using sciling
print(t[4:7])

#output
#3
#7
#(4, 5, 6)
#(5, 6, 7)


t=("preethi","likki","sai","varu")
print(t[3])
print(t[2:3])
print(t[2:3+1])

##output
##varu
#('sai',)
#('sai', 'varu')


## and we can also take different data types in tuple()
t=("preethi",20,33.33,False,True,10,10)
## we can also use duplicate in the tuple
print(type(t))
print(t[4])
print(t[1:4])

#output
#True
#(20, 33.33, False)

## method in tuple
## >> count()
##        >> count is used for count the elements in
#               tuple 
#   >> by using the count we can also find the higest 
#          frequency of elementst
t=("preethi",20,33.33,False,True,20,30,True)
print(t.count(20))
print(t.count(True))
print(t.count(33.33))

## output
#2
#2
#1
#1
#4

## >> index()

t=("preethi",20,33.33,False,True,20,30,True)
print(t.index(20))
print(t.index(True))

#output
 # 1
 # 4

## we can also check the element is present in the tuple or not
t=(1,2,3,5,4,5,6,7,5,8)
print(t.count(5))
print(t.count(4))

## we can get the higest frequency of thge elements by using count()


#output
#3
#1

##operations of tuple :
# > we two operations in tuple addition and repetation
#addition
t=(1,2,3,4)
t1=(5,6,7,8)
print(t+t1)
## by using the additions operator we can the two tuples
#output
#(1, 2, 3, 4, 5, 6, 7, 8)


# repetation
t=("preethi","sai")
t1=("likki","varu")
print(t+t1)
print(t*2)

#output
#('preethi', 'sai', 'likki', 'varu')
#('preethi', 'sai', 'likki', 'varu')

##nested tuple

t=(1,2,3,4,(5,6,7))
print(t[4][1])
print(t[2:4])
print(t[2:4])
print(t[1:5])

#output
#6
#(3, 4)
#(2, 3, 4, (5, 6, 7))

## packing and unpacking of tuple elements
# packing >Packing a tuple means creating a tuple by 
#               grouping multiple values together
p=(33.3,44.4,22.2,55.5,77.7)
(e,d,c,b,a)=p
print(a)
print(c)
print(e)

# unpacking>>Unpacking a tuple means extracting its values 
#                into individual variables

#output
#77.7
#22.2
#33.3

## modifing pf tuple elements 
# we can modify the tuple by using typecasting

t=("preethi",20,"sai",30,101)
l=list(t)
print(l)
print(l.append(True))
print(l)
print(l.index("preethi"))
print(l.pop())
t=tuple(l)
print(t)

#output
#['preethi', 20, 'sai', 30, 101]
#['preethi', 20, 'sai', 30, 101, True]
#0
#True
#('preethi', 20, 'sai', 30, 101)


## tuple comprehenssion:
# >> converter the large number of line into single line
t=(l for l in range(1,20) if (l%2==1))
print(t)

# it will generates the object of the tuple 

print(tuple(t))

## output
#  (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)






