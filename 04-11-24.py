#instance method:
# >we can declaring and accessing a instance variable inside a method
# >while declaring instance method have to pass self as an first paramater
# >we can acces thses instance method using orv or classname
#example:1
class bank:
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
 
    def m(self,acc_no,ph_no):
        self.acc_no=acc_no
        self.ph_no=ph_no
        print(self.name)
        print(self.age)
        print(self.acc_no)
        print(self.ph_no)  
 
d=[]
m1=int(input("enter a number_of:"))  
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))
    bank=bank(name,age)
    d.append(bank)
 
for bank in d:
    bank.m(223,7702616317)                
 

#example:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def wish(self):
        print(self.name)
        print(self.age)
 
    def introduce(self):
        self.wish()
        print("tomorrow is my birthday")
 
person= person("Preethikareddy", 25)
person.introduce()

#example:3
class cat:
    def __init__(self,name,age):
 
        self.name=name
        self.age=age
 
    def m(self,bread):
        self.bread=bread
        print(self.name)
        print(self.age)
        print(self.bread)  
 
c=[]
m1=int(input("enter a number_of:"))  
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))
 
    cat=cat(name,age)
    c.append(cat)
 
for cat in c:
    cat.m("cymric")
 


#class method:
# >inside the class method have  to use only static variable
# >while declaring class method have to pass @class method
# >while declaring class method have to pass cls as first parameter
# > using cls keyword we can declare and can access the data in side class method has context menu

#example:1
class fruit:
    totalprice=2000
    @classmethod
    def m(cls,apple,banana,orange):
        cls.shopname="NPBF"
        print(apple)
        print(banana)
        print(orange)
        print(fruit.totalprice)
        print(cls.shopname)
 
p=fruit()
p.m(3,2,4)

#example:2
class filpkart:
    price=20000
    @classmethod
    def m(cls,name,rating):
        cls.companyname="NPBF"
        print(name)
        print(rating)
        print(cls.companyname)
        print(cls.price)
 
f=filpkart()
f.m("realme narzo","4star")
 
#example:3
class collage:
    branch="cse"
    @classmethod
    def m(cls,name,rollno):
        cls.collagename="preethi"
        print(name)
        print(rollno)
        print(cls.branch)
        print(cls.collagename)
 
c=collage
c.m ("preethi",105)      
 

#static method:
#  >>we are not using instance and static variable
#  >we are not passing any paramter like self or cls
# >we have to pass @staticmethod decorate
# >we can access static method using class anem and cls variable
 
#example:1
class bank:
    @staticmethod
    def m():
        name="Preethika reddy"
        age=25
        phone_no=1000234789
        acc_no=145
        return name ,age,phone_no,acc_no
 
b=bank()
print(b.m())        
 
#example:2

class mul:
    @staticmethod  # >>it is a stasticmethod we acn access directly in the class
    def m():
        a=5
        b=9
        print(a*b)
a1=mul()
a1.m()

#example:3
 
class fruits:
    @staticmethod
    def m():
        apple=1
        guva=2
        banana=3
        pineapple=4
        totaliteams=apple+guva+banana+pineapple
        return totaliteams
f=fruit()
print(f.m())
 
 
 