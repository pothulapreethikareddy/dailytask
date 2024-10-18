#Remove all occurrences of the number 3 from a list of integers


list = [1, 3, 2, 3, 4, 3, 5, 6, 3]
list = [num for num in list if num != 3]
print(list)
