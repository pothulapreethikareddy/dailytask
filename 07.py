#Extends the list with another list of numbers.

list = [list for list in range(1,10+1)]
extend_list = [60, 70, 80, 90]
list.extend(extend_list)
print(list)

