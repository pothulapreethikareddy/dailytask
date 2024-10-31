#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(name):
    return(["Hello,,"+name+"!"])
name=["preethi"]
print(greet(" ".join(name)))

#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add(s1, s2):
    return s1 + s2

print(add(5, 7))
print(add(10, 20))

#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def even(num):
    return num % 2 == 0

print(even(10))
print(even(11))

#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))
print(factorial(5))
#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 20, 30))
print(find_max(2, 2, 2))

#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("Hello World"))

#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
           return False
    return True

print(is_prime(11))
print(is_prime(15))

#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).


def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)


#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

print(calculator(10, 2, "+"))
print(calculator(10, 2, "-"))

#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.

def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]

print(find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello World"))

#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.##
def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])

print(sort_dict_by_value({"a":3,"b":1,"c":2}))
