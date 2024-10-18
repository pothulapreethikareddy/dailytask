#Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.

fruits = ["pineapple","custed apple","mango","watermelon","kiwi"]
print(fruits)
fruits.reverse()
print(fruits)
reversed_fruits = fruits[::-1]
print(reversed_fruits)
print("Comparison:", fruits == reversed_fruits[::-1])
