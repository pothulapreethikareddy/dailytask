##inheritance:
##         >> it is an a parent to child class
 
## single:
#        >>class inheriting from only one parent class
 
 
class p:
    def m1(self):
        print("this is instance method parent classes")
 
class c(p):
    def m2(self):
        print("this child class instace method")
 
c=c()
c.m1()
c.m2()
 
 
 
 
 
 
 
 
 
 
 
 
 
## multiple:
##         >>inheriting properties and methods from multiple classes to single class ot the same class
 
 
class f:
    def m1(self):
        self.nature="hardworking"
 
class m:
    def m2(self):
        self.nature1="kind"
 
class c(m,f):
    def m3(self):
        print(self.nature)
        print(self.nature1)
 
c=c()
c.m1()
c.m2()
c.m3()
 
 
 
 
 
 
 
 
 
## multilevel:
##          >>inheriting properties and methods from multilevel classes to single class
 
 
class gf:
    def m1(self):
        self.land=8
 
class f(gf):
    def m2(self):
        print(self.land)
        self.land=10
 
class c(f):
    def m3(self):
        print(self.land)
        self.land=12
        print(self.land)
 
c=c()
c.m1()
c.m2()
c.m3()
 
 
 
 
 
 
 
 
## hyarchical:
##         >>inheriting properties and methods from single classes the multiple classes
#          >>single class to two child class
 
class p:
    def __init__(self):
        self.land=20
 
class c1(p):
    def m1(self):
        print("child_1",self.land-10)
 
class c2(p):
    def m2(self):
        print("child_2",self.land-10)
 
c1=c1()
c1.m1()
c2=c2()
c2.m2()        
 
 
 
 