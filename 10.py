#Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

list = [list for list in range(1,15+1)]

list.sort()
print("ascending order:",list)
list.reverse()
print("Descending Order:", list)
ascending = sorted(list)


