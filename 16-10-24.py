## set >> set is an collection unorderd and unindex  
#       >>it is mutable
##      >> we cannot change the set elements
##      >>it  dont's allows duplictes

s={}
print(s)
print(type(s))


s={1,2,3,4,"preethi",33.33,True}
print(s)
print(type(s))

#{}
#{1, 2, 3, 4, 'preethi', 33.33}
#<class 'set'>

##adding of element to set
## update() >> update a empty set with a list of elements
#          >>update()


s=set ()
l=["preethi","reddy",1,33.33,True,False]
s.update(l)
print(s)
print(type(s))

##output
##{False, 1, 33.33, 'preethi', 'reddy'}
##<class 'set'>

##add >> we can add the elements in the set and 
#        >> also asscending order
#       >> add()

s={1,3,4,7,69,10,12,45}
s.add(55)
print(s)
print(type(s))

#output
#{1, 3, 4, 69, 7, 10, 12, 45, 55}
#<class 'set'>

#removing of elements in set

#pop()  > it wil remove the first element from the set
#        >> and also it will set the set as asscending order

s={1,2,3,5,6,9}
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

##discard()  >>it will remove the particular 
##              >elements from the set

s={1,"preethi","sai",True}
s.discard(True)
print(s)


#output
#{'preethi','sai', 1}

#clear()
#  > it will clear all the elements in the set

s={1,"preethi"}
s.clear()
print(s)

#delete
#   > it will delete particular element and 
#   > it will delete permentelly

"""s={1,"preethi"} 
del s
print(s)
"""


##remove()   > if the element to remove does not 
#          > it will  show as error

s={1,"preethi"}
s.remove(1)
print(s)



s=(x for x in range(1,11))
print(set(s))



