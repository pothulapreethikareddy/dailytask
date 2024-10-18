#write a program for multiple of 3 print "fizz" instead of number and for multiple of 5 print "buzz"

for i in range(1,100+1):
   if i%3==0:
      print("fizz")
   elif i%5==0:
      print("buzz")
   else:
      print(i)