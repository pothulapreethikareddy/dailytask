###oops : object oriented programming language
#   >> it is a programming paradigm that user objects and classes in the programming
#   >> it is realworld entity which is used in
#         1.classes
#         2.objects
#         3.encapsulations
#         4.inheritance
#         5.polymorphism
#         6. abstraction
 
#importance oop:
# > oops is an code reuseable
# >it is an fundememntal in python has it enhance code reuseablty encapsulations oragransation and scalability
#  >it can be builted as  strong and complex applications
#   > it is scalability and flexibility
 
 
## realtime appliactions
#  > web
#  >gaming
#  > desktop
#  >artificial intelligence and machine learning
#
 
 
## class :
#   >> it is a model or a blueprint
#   >> it is a code template for creating an object
#   >>it is also know as object constructor
 
#     class
 
#class num():
   
 
 
# object:
## >> realtime entity of a class
#  >>  variable that contain data and function that can be used to manipulate the data
##  
 
# n=num() >> n is a object refreance variable
 
##example:
 
class dmart :
 
    def dispaly(self,name):
        print(name,"chocolate")
c=dmart()
c.dispaly("5star")      
 
 
 
class dmart :
    def __init__(self,name,rate,discount,dateofexpired):
        self.name=name
        self.rate=rate
        self.discount=discount
        self.dateofexpired=dateofexpired
    def display(self):
        print(self.name)
        print(self.rate)
        print(self.discount)
        print(self.dateofexpired)
 
d=dmart("5star",50,"20%",24-10-24)
 
d.display()
 
#output
#5star
#50
#20%
#-10
 
 
class showroom:
    def __init__(self,car,brand,model,price,onroadprice,rating):
        self.car=car
        self.brand=brand
        self.model=model
        self.price=price
        self.onroadprice=onroadprice
        self.rating=rating
    def get_details(self):
        print("car -",self.car)
        print("brand -",self.brand)
        print("model -",self.model)
        print("price -",self.price)
        print("onroadprice -",self.onroadprice)
        print("rating -",self.rating)
 
c=showroom("thar","xu4",2024,140000,160000,4.5)
c.get_details()
 
 
#output
#car - thar
#brand - xu4
#model - 2024
#price - 140000
##onroadprice - 160000
#rating - 4.5
 
 
##__init__ it will automatically each and every time the class is to used to crate a new object
 
 
 
class num :
    def add(self,a,b):
        return a+b
    def sub(self,x,y):
        return x-y
    def mul(self,a,b):
        return a*b
    def div(self,c,d):
        return c/d
n=num()
print(n.add(3,5))
print(n.sub(5,8))
print(n.mul(7,4))
print(n.div(6,5))  
 
#ouput
#8
#-3
#28
#1.2
 
class num:
    def even(self,l):
        self.l=l
        even_number=[]
        for i in l:
            if i%2==0:
                even_number.append(i)
        return even_number
    def odd(self,l):
        self.l=l
        odd_number=[]
        for i in l:
            if i%2==1:
                odd_number.append(i)
        return odd_number
    def count(self,l):
        self.l=l
        return len(l)  
 
n=num()
l=[1,2,3,4,5,6,7,8,9]
print(n.even(l))
print(n.odd(l))  
print(n.count(l))      
 
#output
#[2, 4, 6, 8]
#[1, 3, 5, 7, 9]
#9
 
 
 
class company :
    def __init__(self,companyname,address,noofemp,loction,gmail):
        self.companyname=companyname
        self.address=address
        self.noofemp=noofemp
        self.location=loction
        self.gmail=gmail
    def get_detalis(self):
        print("companyname -",self.companyname)
        print("address -",self.address)
        print("noofemp -",self.noofemp)
        print("location -",self.location)
        print("maill -",self.gmail)
 
c=company("skywave","opposite to AMB mall",230,"hyderabad","@skywavessoftware.com")
 
c.get_detalis()
 
 
 
""""class shop:
    def __init__(self,
"""""
 
 
class order:
    def __init__(self,sname,totalrate,order_id,discount,payment_id):
        self.sname=sname
        self.totalrate=totalrate
        self.order_id=order_id
        self.discount=discount
        self.payment_id=payment_id
    def get_detalis(self):
        print(self.sname)
        print(self.totalrate)
        print(self.discount)
        print(self.order_id)
        print(self.payment_id)
 
s=order("book",230,"5%",10,"upi")
s.get_detalis()        
 
 
 