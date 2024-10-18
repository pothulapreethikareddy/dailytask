#write a program the task a number as input and print in the sum of its digits

n = eval(input("enter a number:"))
digits = 0
digit_sum = 0
temp = n  
while temp > 0:
    digit = temp % 10  
    digit_sum += digit  
    digits += 1         
    temp //= 10         
 
print(digits)
print(digit_sum)