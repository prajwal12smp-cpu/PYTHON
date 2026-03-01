#input() function is used to take input from the user#input() function is used to take input from the user
#syntax: variable_name = input("prompt message")

name = input("Enter your name: ") #this will take input from the user and store it in the variable 'name'
age = input("Enter your age: ") #this will take input from the user and store it in the variable 'age'
gender = input("Enter your gender: ") #this will take input from the user and store it in the variable 'gender'
price = input("Enter the price of the item: ") #this will take input from the user and store it in the variable 'price'
quantity = input("Enter the quantity of the item: ") #this will take input from the user and store it in the variable 'quantity'
total_price = float(price) * int(quantity) #this will calculate the total price by multiplying the price and quantity

print("Hello, " + name + "!") #this will print the message along with the name entered by the user
print("You are " + age + " years old.") #this will print the message along with the age entered by the user
print("You are " + name + " and you are " + age + " years old and your gender is " + gender)
print("The price of the item is " + price) #this will print the message along with the price entered by the user
print("The quantity of the item is " + quantity) #this will print the message along with the quantity entered by the user
print("The total price of the item is " + str(total_price)) #this will print the message along with the total price calculated


