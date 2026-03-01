#tType conversion in python
#Type conversion is the process of converting one data type to another data type in Python.
#There are two types of type conversion in Python:
#1. Implicit Type Conversion: Python automatically converts one data type to another data type.
#2. Explicit Type Conversion: The user manually converts one data type to another data type.

#Example of Implicit Type Conversion
a = 5 # Integer
b = 2.5 # Float
c = a + b # The result will be a float because Python automatically converts the integer to a float.
print(c) # Output: 7.5

#Example of Explicit Type Conversion
a = "10" # String
b = int(a) # Convert string to integer
c = float(b) # Convert integer to float
print(c) # Output: 10.0

#Example of Explicit Type Conversion using input() function
name = input("Enter your name: ") # Input is always a string by default
age = int(input("Enter your age: ")) # Convert string to integer
print("Your name is:", name)
print("Your age is:", age)
