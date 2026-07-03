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