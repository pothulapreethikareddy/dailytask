## set{}
## union()
## It will add two set elements without duplicates
 
s1={"preethi","keerthi",1,2,3,45}
s2={"ajji","reddy",2,3,4}
print(s1.union(s2))
 
##output
##{1, 2, 3, 4, 'ajji', 'preethi', 45, 'reddy', 'keerthi'}
 
##intersection()
##  > It will retuns only commom elements in the set
 
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
print(s1.intersection(s2))
 
#output
#{8, 9}
 
##intersection_update()
## >>   It modify the set that are have only common elemnets in the both the sets
 
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
s3=s1.intersection_update(s2)
print(s3)

##difference()
##  > returns s1 elements which are not present in s2
 
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
print(s1.difference(s2))
 
##output
##{'preethi', 78, 'keerthi'}
## 8,9 is present in the s1 and s2 also
 
## difference_update()
##   >It modifies the original set by removing elements that are present in another specified set
 
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
print(s1.difference_update(s2))
 
## symetric_difference()
## >> It returns both s1 ans s2 which are not present in both the sets
 
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
print(s1.symmetric_difference(s2))
 
 
#output
#{'reddy', 'ajji', 10, 'keerthi', 'preethi', 78}


##symetric_diffrence_update()
s1={"preethi","keerthi",78,8,9}
s2={"ajji","reddy",8,9,10}
print(s1.symmetric_difference_update(s2))
 
 
##modifying of set elements
s={1,2,3,4,5,6,7}
l=list(s)
print(l)
l.append(9)
print(l)

#output:
#[1, 2, 3, 4, 5, 6, 7]
#[1, 2, 3, 4, 5, 6, 7, 9]
 