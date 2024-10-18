#Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.

list = [1, 2, 3, 4, 5]
print(list)
assigned_list = list
print(assigned_list)
list.append(6)
print(list)
copy_list = list.copy()
print(copy_list)

