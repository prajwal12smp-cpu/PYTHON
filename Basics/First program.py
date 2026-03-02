# This is a simple Python program that prints "Hello, World!" to the console.
print("Hello, World!")

# This program demonstrates basic string output in Python.
print("Welcome to Python programming! Prajwal ")
print("My age is 21 years old.")

# You can also combine multiple strings in a single print statement.
print("Prajwal is my name", "My age is 21 years old")

# You can print numbers as well.
print(23)
print(35)

 
 # You can also use variables to store values and perform operations on them.
name = "Prajwal Shivashimpar" # String variable to store a name
age = 21 # Integer variable to store age
price = 19.99 # Float variable to store price
print(name)
print(age)
print(price)
print("My name is :", name)
print("My age is :", age)
print("The price of the item is :", price)

#Rules for Identifiers in Python:
# 1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. An identifier cannot start with a digit.
# 3. An identifier cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.).
# 4. An identifier is case-sensitive (e.g., myVariable and MyVariable are different).
# 5. An identifier should not contain spaces (use underscores instead).
# 6. Identifiers can be of any length, but it is recommended to keep them concise and meaningful.
# 7. we cannot use special characters like @, #, $, etc. in identifiers.

#Data types in python:
# 1. int: Represents integer values (e.g., 1, -5, 0).
# 2. float: Represents floating-point numbers (e.g., 3.14, -0.5).
# 3. str: Represents strings, which are sequences of characters (e.g., "Hello", 'Python').
# 4. bool: Represents boolean values, which can be either True or False.
# 5. none: Represents the absence of a value or a null value (e.g., None).

name = "Prajwal Shivashimpar" 
age = 21 
price = 19.99
print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(price)) # Output: <class 'float'>

age = 21
old = False
a = None
print(type(old)) # Output: <class 'bool'>
print(type(a)) # Output: <class 'NoneType'>


#keywords in Python:
# Python has a set of reserved keywords that cannot be used as identifiers (variable names, function names, etc.) because they have special meanings in the language. Here is a list of Python keywords:
# 1. False
# 2. None
# 3. True
# 4. and
# 5. as
# 6. assert
# 7. break
# 8. class
# 9. continue
# 10. def
# 11. del
# 12. elif
# 13. else
# 14. except
# 15. finally
# 16. for
# 17. from
# 18. global
# 19. if
# 20. import
# 21. in
# 22. is
# 23. lambda
# 24. nonlocal
# 25. not
# 26. or
# 27. pass
# 28. raise
# 29. return
# 30. try
# 31. while
# 32. with
# 33. yield


#print sum of two numbers
a = 10
b = 20
sum = a + b
print(sum)

#difference of two numbers
diff = a - b
print(diff)

#product of two numbers
product = a * b
print(product)


#comments in python:
# This is a single-line comment in Python.

"""
This is a multi-line comment in Python.
It can span multiple lines and is useful for providing detailed explanations
about the code's functionality or purpose.
"""

#Types of operators in python:
# 1. Arithmetic Operators: +, -, *, /, %, **, //
# 2. Relational / Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=

#Example of using arithmetic operators
x = 5
y = 2
print(x + y)  # Output: 7
print(x - y)  # Output: 3
print(x * y)  # Output: 10
print(x / y)  # Output: 2.5
print(x % y)  # Output: 1
print(x ** y) # Output: 25
print(x // y) # Output: 2

#Example of using relational / comparison operators
a = 50
b = 30
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

#Example of using assignment operators
num = 10
num = num + 10 # Equivalent to num += 10
print(num)  # Output: 20

num = 20
num = num - 10 # Equivalent to num -= 10
print(num)  # Output: 10

num = 10
num = num * 10 # Equivalent to num *= 10
print(num)  # Output: 100

num = 100
num = num / 10 # Equivalent to num /= 10
print(num)  # Output: 10.0

num = 10
num = num % 3 # Equivalent to num %= 3
print(num)  # Output: 1

num = 2
num = num ** 3 # Equivalent to num **= 3
print(num)  # Output: 8

num = 10
num = num // 3 # Equivalent to num //= 3
print(num)  # Output: 3


#Example of using logical operators
x = 5
y = 10
print(x > 3 and y < 15)  # Output: True
print(x > 3 or y < 5)    # Output: True
print(not(x > 3 and y < 15))  # Output: False
