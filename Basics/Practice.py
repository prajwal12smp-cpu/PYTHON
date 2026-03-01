#write a program to input 2 numbers and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("The sum of", a, "and", b, "is", sum)


#write a program to input side of a square and print its area.
side = float(input("Enter the side of the square: "))
area = side * side
print("The area of the square is", area)


#write a program to input 2 floating point numbers and print their average.
num1 = float(input("Enter first floating point number: "))
num2 = float(input("Enter second floating point number: "))
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is", average)


#write a program to input 2 int numbers, a and b. Print true if a is greater than or equal to b, otherwise print false.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
if a >= b:
    print("True")
else:
    print("False")
