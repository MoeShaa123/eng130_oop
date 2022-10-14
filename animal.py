
# create a class called Animal - file-name start with a - class name starts with A
# add the common attributes/var behavior/ functions
# syntax class name: - class Animal:

class Animal: # follow the correct naming convention & best practices
    # we need to initialise it with builtin method called __init__(self)
    # self refers current class
    def __init__(self): # any attributes attached to the class should be part of init method
        # self.var = True
        self.alive = True
        self.spine = True
        self.eyes = True

# let's create some methods to add common behaviors
    def breathe(self):
        return "keep breathing to stay alive"
# let's add one more behavior
    def eat(self):
        return "time to eat! ..."

# create an object of this class
cat = Animal() # creating an object of our Animal classes
# print(cat.breathe()) # calling a method using object of the Animal class
# print(cat.eat())