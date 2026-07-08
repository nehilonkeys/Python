import math

# # this is my first python program
# print("Hello, World!")
# print("It's really good!")

# #variable = A container for a value (string, integer, float, boolean)
# #           A variabe behaves as if it was the value it contains

# #Strings
# first_name = "Nick"
# food = "Pizza"
# email = "nick@example.com"
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is {email}")

# #integers
# age = 21
# quantity = 3
# num_of_students = 30
# print(f"You are {age} years old")
# print(f"You have {quantity} items in your cart")
# print(f"There are {num_of_students} students in the class")

# #Floats
# price = 9.99
# pi = 3.14
# gpa = 3.5
# distance = 5.2
# print(f"The price is ${price}")
# print(f"The value of pi is {pi}")
# print(f"Your gpa is {gpa}")
# print(f"You ran {distance} miles")

# #Booleans
# #is_online = input("Are you online? (True/False): ")
# #if is_online == "True":
# #    print("The user is online")
# #else:
# #    print("The user is not online")

# #Typecasting =teh process of converting a variable from one data type to another str(), int(), float(), bool()
# name = "Nick"
# age = 21
# gpa = 3.5
# is_student = True

# gpa = int(gpa)
# print(gpa)

# age = float(age)
# print(age)

# age = str(age)
# print(type(age))

# #age += 1 
# #Error TypeError: can only concatenate str (not "int") to str

# age += "1"
# print(age)


# # input() = A funtion that allows user input to enter data and returns the entered data as a string
# #name = input("What is your name? ")
# #age = input("How old are you? ")
# #print(f"Hello {name}, you are {age} years old")

# #age = int(age)
# #age = age+1
# #print("HAPPY BIRTHDAY!")
# #print(f"{name}, you are now {age} years old")





# #Exercise 1 Rectangle Area Calculator
# #length = input("Enter the length of the rectangle: ")
# #width = input("Enter the width of the rectangle: ")
# #length = float(length)
# #width = float(width)
# #area = length * width
# #print(f"The area of the rectangle is: {area}cm^22")



# #Exercise 2 Shopping Cart Program
# #item = input("What item would you like to buy?: ")
# #price = float(input("What is the price of the item?: "))
# #quantity = int(input("How many items would you like?: "))
# #tax= float((price*quantity)*0.074)
# #subtotal = (price * quantity)
# #total = subtotal+tax
# #print(f"You bought {quantity} {item}(s) at ${price} each")
# #print(f"Your total for {item} is ${total} (including tax)")



# # Matlib game
# # word game where you create a story
# # by filling in the blanks with random words
# #noun = input("Enter a noun: ")
# #verb = input("Enter a verb: ")
# #adverb = input("Enter an adverb: ")
# #adjective = input("Enter an adjective: ")
# #animal = input("Enter an animal: ")
# #print(f"Today I went to a {adjective} zoo. I saw a(n) {adjective} {animal} jumping up and down in its tree. He {verb} {adverb} through the large tunnel that led to its {adjective} {noun}. I got some peanuts and passed them through the cage to a gigantic gray {animal} towering above my head. Feeding that animal made me hungry. I went to get a {adjective} scoop of ice cream. It filled my stomach. Afterwards I had to {verb} {adverb} to catch our bus. When I got home I {verb} my mom for a {adjective} day at the zoo.")




# #arithemic operators = + - * / % ** //
# #math fuynctions = round(), abs(), pow(), min(), max()
# #exercises

# friends = 5
# friends = friends + 1
# # friends =+ 1
# print(friends)

# friends = friends - 1
# #friends -= 1
# print(friends)

# friends = friends * 3
# #friends *= 3
# print(friends)

# friends = friends / 2
# #friends /= 2
# print(friends)

# friends = friends ** 2
# #friends **= 2
# print(friends)

# friends = friends / 2
# #friends /= 2
# print(friends)

# friends = friends % 2
# #friends %= 2
# print(friends)

# friends = friends // 2
# #friends //= 2
# print(friends)


# x = 3.14
# y = -4
# z = 5

# #round
# result = round(x)
# print(result)

# #absolute value
# result = abs(y)
# print(result)

# #power
# result = pow(z, 2)
# print(result)

# #max
# result = max(x, y, z)
# print(result)

# #min
# result = min(x, y, z)
# print(result)



# print(math.pi)
# print(math.e)
# print(math.sqrt(16))
# result = math.ceil(3.4)
# print(result)
# result = math.floor(3.4)
# print(result)


# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {circumference}")
# print(f"The circumference of the circle is: {round(circumference, 2)}cm")

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {area}cm^2")
# print(f"The area of the circle is: {round(area, 2)}cm^2")

#find hypotenuse of a right triangle using pythagorean theorem c=sqrt(a^2 + b^2)
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a,2) + pow (b, 2))
# print(f"side c = {c}")

# if = Do some code only IF some condition is True
#      Else do something else
# age = int(input("What is your age?: "))
# if age >= 18 and age < 80:
#     print("You are an adult(bade loog)")
#     print("You have access to this content")
# elif age >=13 and age <18:
#     print("You are a teenager(tu thodi deer aur ther ja ))")
#     print("You have limited access to this content (baad mein ana gandu)")
# elif age >=80:
#     print("You are a senior citizen(budha ho gaya hai re tu))")
#     print("You are too old to have access to this content")
# else:
#     print("You are a child(baccha hai re tu))")
#     print("You must be 18 or older to have access to this content")

# python calculator
# operation = input("Enter operation (+, -, *, /): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print(f"You entered: {num1} {operation} {num2}")
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# print(f"Result: {result}")



# python weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Enter unit (K for kilograms or L for pounds): ")
# if unit == "K":
#     weight = weight * 2.20462
#     unit = "Lbs"
#     print(f"your weight is {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.20462
#     unit = "Kgs"
#     print(f"your weight is {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} is not a valid unit")
#     print("Please enter K for kilograms or L for pounds")


# temperature converter
# temp = float(input("Enter the temperature: "))
# unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
# if unit == "C":
#     temp = (temp * 9/5) +32
#     unit = "F"
#     print(f"The temperature is {round(temp, 1)} {unit}°")
# elif unit == "F":
#     temp = (temp - 32) * 5/9
#     unit = "C"
#     print(f"The temperature is {round(temp, 1)} {unit}°")
# else:
#     print(f"{unit} is not a valid unit")
#     print("Please enter C for Celsius or F for Fahrenheit")


# logical operators = and, or, not (evalute multiple conditions)
#                  or = at least one condition is true
#                  and = both or all the conditions are true
#                  not = reverses the result, returns False if the result is true


# temp = float(input("Enter the temperature: "))
# is_raining = True (select this or the second one to test the code)
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("The weather is bad today")
# else:
#     print("The weather is good today")


# temp = float(input("Enter the temperature: "))
# is_sunny = True
# if temp > 30 and is_sunny:
#     print("The weather is hot and sunny today")
# elif temp < 0 and is_sunny:
#     print("The weather is cold outside and sunny today")
# elif temp < 0 and not is_sunny:
#     print("The weather is cold outside and not sunny today")
# elif temp > 30 and not is_sunny:
#     print("The weather is hot outside and not sunny today, its little humid")
# so on 


# condition expression = A one-line shortcut for the if-else statement (ternary operator)
#                       Print or assign one of two values based on a condision
#                       X if condition else Y

# num = -5
# print("Positive" if num>0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# a=input("Enter a number for a: ")
# b=input("Enter a number for b: ")
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)  

# age = 13
# status = "Adult" if age >= 18 else "Child"
# print(status)

# temperature = 19
# weather = "Hot" if temperature > 20 else "Cold"
# print(weather)

# user_role = "admin"
# user_role = "guest"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(access_level)




#String methods
# name = input("Enter your full name: ")
#Nehil Patel
# result = len(name)  = 11
# result = name.find("e")  = 1
# result = name.rfind("e") = 9
# result = name.rfind("w") = -1
# result = name.capitalize() = Enter your full name: Nehil Patel
#                              Nehil patel
# result = name.upper()
# Enter your full name: Nehil Patel
# NEHIL PATEL
# result = name.lower()
# Enter your full name: NEHIL PATEL
# nehil patel
# result = name.isdigit()
# Enter your full name: 123
# True 
# result = name.isalpha()
# Enter your full name: Nehil Patel it has space so the result will be false
# False
# result = name.isalpha()
# Enter your full name: NehilPatel
# True
# print(result)
# phone_num = input("Enter your phone number: ")
# result = phone_num.count("-")
# Enter your phone number: 1-234-4567-7890
# 3
# phone_num = input("Enter your phone number: ")
# phone_num = phone_num.replace("-"," ")
# Enter your phone number: 1-234-567-8901
# 1 234 567 8901
# print(phone_num)

## just an info write 
# print(help(str))



# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter a username: ")

# if len(username) > 12 or username.rfind(" ") != -1 or username.isdigit:
#     print("Something went wrong please try again")
# else:
#     print(f"Welcome {username}")


#indexing = accessing elements of a sequence using [] (indexing operator)
            # [start : end : step]
# creditcard_num = "1234-5678-9012-3456"

# print(creditcard_num[0])
# print(creditcard_num[0:4])
# print(creditcard_num[0:19])
# print(creditcard_num[0:19:2])
# print(creditcard_num[::-1])
# last_digits = creditcard_num[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# format specifiers = {value:flags} format a value based on what
                    # flags are inserted
# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma

# price1 = 3000.1234
# price2 = 9870.1234
# price3 = -1200.1234

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.3f}")
# print(f"Price 1 is ${price1:20}")
# print(f"Price 2 is ${price2:>20}")
# print(f"Price 3 is ${price3:<20}")
# print(f"Price 1 is ${price1:^20}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:-}")
# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,.2f}")




#while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You didn't enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")



# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old!")



# food = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit): ")
# print("Bye")



# num = int(input("Enter a # between 1 - 10: "))
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))
# print(f"Your number is {num}")



# Python compound intrest calculator
