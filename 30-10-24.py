# types of variables:
## 1.instance variables:
##    >>declarations:
#          >>varable that changes from object to object
#          >>it is created by self keywords
#         >> we can create instance variables inside of constructor and instance method
#
#     >>accesing :
#         >>we can access instance variable class by using self keyword
#         >>we can access outside of the class  using ORV(object refrence variable)
#
 
class emp:
    def __init__(self):
        self.name="preethi"
        self.salary=24000
 
    def dispaly(self,age,id):
        self.age=age
        self.id=id
        print(self.name)
        print(self.salary)
       
 
e=emp()
e.dispaly(20,203)
print(e.name) # we can access outside the class
print(e.age)
 
 
 
 
class collage:
    def __init__(self,name,branch,rollno,classno,blockno):
        self.name=name
        self.branch="ece"
        self.rollno=rollno
        self.classno=classno
        self.blockno=blockno
 
    def s(self):
        print(self.branch)
        print(self.name)
        print(self.rollno)
        print(self.classno)
        print(self.blockno)
c=collage("preethi","ece",27,203,1105)
c.s()
 
c1=collage("keerith","ece",23,205,1999)
c1.s()
 
 
 
 
class cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
    def c(self):
        print(self.name)
        print(self.age)
 
c1=cow("chaint",3)
c1.c()
c2=cow("cat",2)
c2.c()        
 
 
 
 
#static variable:
#   >>declaration:
#        >>in static variable is not changing object to object
#       >>we can declare a static variable inside the class directly
#       >>inside the constructor ,instance methode using classname
#       >>outside of class using class name
#       >>inside the class methose using class variable
#
#    >>accessing :
#         >>using class name we can access inside the constructor and instance method
#         >>outside of a class using classname and ORV
#         >>inside of the class method using class variable
#  
#
 
class collage:
    collagename="avr collage"  ##we can declare a static variable inside the class directly
    def __init__(self,name,branch,rollno):
       
        self.name=name
        self.rollno=rollno
       
        collage.branch="ece branch"  # inside the constructor ,instance methode using classname
       
        print(collage.branch) # class name we can access inside the constructor and instance method
   
    def d(self):
        collage.section="section d"
        print(self.name)
        print(self.rollno)
       
 
s=collage("preethi","ece",27)
print(collage.collagename)
 
collage.age=20  ## outside of a class using classname and ORV  
s.d()  
print(collage.age)  
 
 
 
 
 
class cow:
    cowbread="hf"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        cow.legs="4 legs"
 
    def c(self):
        cow.eyes="2 eyes"
        print(self.name)
        print(self.age)
s=cow("chanti",2.5)
s.c()
print(cow.cowbread)
print(cow.legs)
print(cow.eyes)