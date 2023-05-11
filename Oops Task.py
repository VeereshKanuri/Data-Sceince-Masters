#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
class vehicle:
    def __init__(self,name_of_vehicle, max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle


# In[2]:


#2
class car(vehicle):
    def seating_capacity(self,capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} people."


# #3
# Multiple inheritance is a feature of object-oriented programming languages like Python that allows a class to inherit properties and methods from more than one parent class.
# 
# In Python, multiple inheritance is achieved by defining a class that inherits from two or more classes. When an object of this class is created, it inherits properties and methods from all its parent classes.
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         
#     def speak(self):
#         pass
# 
# class Mammal(Animal):
#     def __init__(self, name):
#         super().__init__(name)
# 
#     def speak(self):
#         return "Mammal speaks"
# 
# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name)
# 
#     def speak(self):
#         return "Bird speaks"
# 
# class Bat(Mammal, Bird):
#     def __init__(self, name):
#         super().__init__(name)
# 
# b = Bat("Batman")
# print(b.speak())
# 

# #4
# In Python, getters and setters are methods used to get and set the values of an object's attributes. Getters are used to retrieve the value of an attribute, and setters are used to set the value of an attribute. They are commonly used in object-oriented programming to control access to an object's attributes and ensure data encapsulation.
# 
# Here is an example class in Python that demonstrates the use of a getter and a setter:
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     
#     def get_name(self):
#         return self._name
#     
#     def set_name(self, name):
#         self._name = name
#         
#     def get_age(self):
#         return self._age
#     
#     def set_age(self, age):
#         self._age = age
# In the above example, the Person class has attributes _name and _age. The class has getter and setter methods for both attributes. The getter methods are named get_name() and get_age(), while the setter methods are named set_name() and set_age().
# 
# The underscore prefix in _name and _age indicates that these attributes are intended to be private. This means that they should not be accessed directly from outside the class. Instead, the getter and setter methods are used to access and modify their values.

# #5
# Method overriding is a feature of object-oriented programming in which a subclass provides its own implementation of a method that is already defined in its superclass. When the method is called on an instance of the subclass, the implementation in the subclass is used instead of the implementation in the superclass.
# 
# class Animal:
#     def make_sound(self):
#         print("The animal makes a sound")
# 
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
# 
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
# 
# a = Animal()
# c = Cat()
# d = Dog()
# 
# a.make_sound() # Output: The animal makes a sound
# c.make_sound() # Output: Meow!
# d.make_sound() # Output: Woof!
# 
