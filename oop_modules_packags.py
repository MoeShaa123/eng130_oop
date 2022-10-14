
# Luck draw
# keyword called import

# There are many built-in modules that can be used in python
from random import *
import math
import datetime, sys
import os
# print(random())
# each time it's run it generates a random number from 0-1

# calculate DOB or year of birth
number = 23.66
# any numbers - to round the figure up
# number 1.5 or above to round up to 2
# number 1.49 or less round down to 1

print(math.ceil(number))  # ceil will help round up the number
print(math.floor(number)) # floor will help round down the number

print(os.cpu_count())  # prints the number of cpu's
print(datetime.date.today())  # prints today's date
print(sys.path) # shows the current directory

# Let's build some functions
# Functions are used so you don't repeat yourself (DRY)
# resusable - saves time - saves money
# syntax def name():

def greeting():
    # greet the user
    print("Hello Dear")
    # pass
    # keyword called pass
# unless the function is called it does nothing
greeting()


def greet_user(name):  # create a function that takes an argument - the name
    print("Hello Dear " + name)

greet_user("Mohamed")

def add(a,b):  # create a function that takes int as an args and add them
    print("this function provides addition")
    return (a+b) # return statement stores the data without printing

print(add(53,5)) # you need to include print statement when calling]

def multiply(a,b):
    print("This will multiply both numbers")
    return (a*b)

def divide(a,b):
    print("This will divide the first number by the second")
    return (a/b)

def remainder(a,b):
    print("This will find the remainder from the first number divided by the second")
    return (a%b)

print(multiply(20,5))
print(divide(20,5))
print(remainder(20,5))

def convert(cm):
    meter = cm/100 # convert CM to M
    print(meter)

convert(231)

def movie_rating(age):
    if age >= 117:
        print("Please re-enter your age")
    elif age >= 18:
        print("You can buy any ticket")
    elif  16 <= age < 18:
        print("you can buy a general ticket")
    elif   12 <= age < 16:
        print("you can't watch restricted content")
    else:
        print("you can only watch PG movies")
    return f"Your age is {age}"

age = int(input("Enter your age: "))
print(movie_rating(age))

def your_age(age):

    current_year = int(2022)
    birth_year = current_year - age
    return (f"You were born in {birth_year}")

age = int(input("Enter your age: "))
print(your_age(age))



def num(range):
    for num in range(1,101):
     #check that the number is divisible by both 3 and 5
        if(num%3==0 and num%5==0):
            print ("FizzBuzz")
        #check that the number is divisible by 3
        elif(num%3 == 0):
            print ("Fizz")
        #check that the number is divisible by 5
        elif(num%5 == 0):
            print ("Buzz")
        #if it's not divisible by either 3 or 5 print the number
        else:
            print(num)

num(range)

def waiter(order):
    menu = ("coke", "fanta", "burger", "pasta", "rice", "chicken", "cake")
    print(menu) # Here's the menu
    current_order = [] # first create an empty list

    # customer greeting
    # print("Hello, thank you for entering our restaurant, what would you like to order?")
    while len(current_order)<3:  # you can only order three items
        order = input("What would you like to order?: ")   # input the order
        if order in menu:

            current_order.append(order) # adds to the order list
            print("anything else?")
            print(f"So you have ordered {current_order}")
        else:
            print("item not in the menu") # if item not in menu print this

order = input("Would you like to look at our menu?: ")
waiter(order)


