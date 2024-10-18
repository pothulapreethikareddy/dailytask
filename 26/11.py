#write a program that counts the number of even and odd number in a list

n = [44,22,58,60,77,14,32,57,102,105]
even_count = 0
even_number=[]
odd_count = 0
odd_number=[]
for i in n:
    if i % 2 == 0:
        even_number.append(i)
        even_count += 1  
    else:
        odd_number.append(i)
        odd_count += 1
print(even_count)
print(even_number)
print(odd_number)
print(odd_count)