# Classes:


# Intro to Classes:
"""
Think of Class like a cookie cutter. 

Python already has built in cookie cutters, so to speak where you can create an integer, strings, and when you create a Class, you are creating your own data type.
"""


class Cookie:  # We start with class and then Title case name to our class

    # Under class Cookie is our constructor which is a method(since has self as parameter) that initializes the creation process of the class
    def __init__(self, color):
        # Color being a parameter that will be passed in has to be declared in this fashion(self.parameter = parameter)
        self.color = color

    # Here is a method we can use that allows us to call it on the instances created to return the color of each cookie created.
    def get_color(self):
        return self.color
    # Here is another method which allows us to re-set the color of an already made cookie instance as shown below (cookie_one.set_color('yellow'))

    def set_color(self, color):
        self.color = color


# Creates a green Cookie and saves it to variable named cookie_one
cookie_one = Cookie('green')

# Creates a blue Cookie and saves it to variable named cookie_two
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())  # Cookie one is green
print('Cookie two is', cookie_two.get_color())  # Cookie two is blue

# Here we are changing cookie_one from being green to being yellow.
cookie_one.set_color('yellow')

# Cookie one is now yellow
print('\nCookie one is now', cookie_one.get_color())
# Cookie two is still blue
print('Cookie two is still', cookie_two.get_color())


# Classes on a Linked List:

# Example of how to use class with a Linked List

"""
  class LinkedList:
    def __init__(self, value):
      
    def append(self, value): # To add an element to the end of the list
      
    def pop(self): # To remove the last element of the list
      
    def prepend(self, value): # To add an element to the beginning of the list
    
    def insert(self, index, value): # To add an element to a specific index in the list
      
    def remove(self, index): # To remove an element to a specific index in the list
"""

# Pointers:

# Pointers on Integers

num1 = 11  # Here we declared the variable num 1 to be equals to 11

num2 = num1  # And now variable num2 to is going to be equal to 11

print("Before num2 value is updated:")
print("num1 =", num1)  # num1 = 11
print("num2 =", num2)  # num2 = 11

print("\nnum1 points to:", id(num1))  # num1 points to: 4343900784
print("num2 points to:", id(num2))  # num2 points to: 4343900784


num2 = 22  # Now we change num2 to be equal to 22 rather than num1

print("\nAfter num2 value is updated:")
print("num1 =", num1)  # num1 = 11
print("num2 =", num2)  # num2 = 22

print("\nnum1 points to:", id(num1))  # num1 points to: 4343900784
print("num2 points to:", id(num2))   # num2 points to: 4343901136

# This shows us that when it comes to integers, in Python they are immutable (they can not be changed). Once you put number 11 into a place in memory, you cannot change that number 11. You can point the variable to a different integer that is stored at a different id, but you can't actually change number 11 that is stored in id 4343900784.


#####################################

# Pointers on Dictionaries

dict1 = {
    'value': 11
}

dict2 = dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)  # dict1 = {'value': 11}
print("dict2 =", dict2)  # dict2 = {'value': 11}

print("\ndict1 points to:", id(dict1))  # dict1 points to: 4346549312
print("dict2 points to:", id(dict2))   # dict2 points to: 4346549312

dict2['value'] = 22  # Now we change dict2's value to be equal to 22 from 11

print("\nAfter value is updated:")
print("dict1 =", dict1)  # dict1 = {'value': 22}
print("dict2 =", dict2)  # dict2 = {'value': 22}

print("\ndict1 points to:", id(dict1))  # dict1 points to: 4346549312
print("dict2 points to:", id(dict2))  # dict2 points to: 4346549312

# This shows us that when it comes to dictionaries, they can change from there original value. Unlike integers that are immutable and can not be changed, here we see the dictionaries are still pointing to the same place in memory (id) from when the value was 11 even though now their value is 22.


# Why is this important?:

"""
  The reason why this is important for DSA is that this concept comes up a lot. For example, with linked list, the nodes on a linked list are going to operate very much like a dictionary.
  
  So if we have two variables pointing at the same node, we can change the value of that node. For example, if we have node_a = 22 and node b and c are pointing to it:
  
    node_a = 22
    node_b = node_a
    node_c = node_a
    
    Now if node_a gets updated to 44 and since node_b and node_c are pointing to it, they will also have a value of 44.
    node_a = 44
    
    In other words, they are still going to point at node_a at the same location and take the value from it.
  
"""

# Garbage Disposal

"""
  Let's say our dictionaries or node variable are now all pointing to one value and stopped pointing to another, what happens to that value? 
  
  In python the unpointed value gets removed in a process that is called garbage disposal.
  
  dict1 -> {"value": 22}       'Garbage disposal' -> {"value": 22}       
  
  dict2 -> {                          dict1 -> {
  dict3 ->  "value": 33               dict2 ->  "value": 33
           }                          dict3 -> }
"""
