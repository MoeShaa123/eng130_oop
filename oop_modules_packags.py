
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







