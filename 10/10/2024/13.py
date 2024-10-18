#Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.


list = [1, 2, 3, 4, 5]
alias_list = list
cloned_list = list.copy()
print(list)
print("Alias List:", alias_list)
print("Cloned List:", cloned_list)

# Modify original list
list.append(6)
print(list)

# Modify alias list
alias_list[0] = 10

# Print updated lists
print(list)

# Modify cloned list
cloned_list[0] = 20

# Print updated lists
print(list)


