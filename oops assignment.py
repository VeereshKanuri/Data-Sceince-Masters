#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question #1 
#In object-oriented programming (OOP), a class is a blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects of the class will have. An object, on the other hand, is an instance of a class. It's a real-world entity that has certain attributes and can perform certain actions (methods) based on the class definition.
#Ex:
Class Animal:
        def __init__(self,breed,name,color):
              self.breed = breed
              self.name=name
              self.color=color
      def bark():
            print(“owee owee”)
#creating object 
dog1=Animal(“german shepherd”,”tommy”,”brown”)
dog1.bark()
#question#2
#Encapsulation : keeping the internal working of an objects hidden from outside world.it is achieved  by defining the attributes and methods of a class as either public,private or protected 
#ex:
    class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.__balance = balance  # make balance private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
#Inheritance:child  inheriting the attributes or methods from a parent class
ex:class Vehicle:
    def __init__(self, num_wheels, fuel_type):
        self.num_wheels = num_wheels
        self.fuel_type = fuel_type

    def start(self):
        print("Starting the vehicle")


class Car(Vehicle):
    def __init__(self, num_wheels, fuel_type, brand, model):
        super().__init__(num_wheels, fuel_type)
        self.brand = brand
        self.model = model

    def drive(self):
        print("Driving the car")

#Here class car(child class is inheriting attributes num_wheels,fuel_type and method  start from parent class vehicle

Polymorphism:it is the ability of an object to take on different forms or behaviour depending on the context in which it is used.
EX:class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

#Above code is an example of polymorphism in which area method is overidden(same method name but different parameters) in different classes

#Abstraction:hiding unnecessary implementation details while exposing only the necessary features of an object.
#ex:
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting car...")

    def stop(self):
        print("Stopping car...")

class Motorcycle(Vehicle):
    def start(self):
        print("Starting motorcycle...")

    def stop(self):
        print("Stopping motorcycle...")

#question#3
#Python, the __init__() function is a special method that is called when an object is created. It is used to initialize the attributes of the object with default or provided values.
#ex:
    class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print(rect.area())      # Output: 50
print(rect.perimeter()) # Output: 30

#question#4
#In Object-Oriented Programming (OOP), self is a reference to the instance of a class. It is used to access the attributes and methods of an instance from within the class.
Ex:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("My name is {} and I am {} years old.".format(self.name, self.age))

person = Person("John", 30)
person.introduce() # Output: My name is John and I am 30 years old.

#question#5 
#inheritance is a mechanism that allows a new class to be based on an existing class, inheriting its attributes and methods. The existing class is known as the parent or base class, and the new class is known as the child or derived class.
#Single inheritance
#Multiple inheritance
#Multi-level inheritance
#Hierarchical inheritance
#1)single inheritance
#Ex:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
#2.multiple inheritance
#Ex:
class Base1:
    def foo(self):
        return "foo from Base1"

class Base2:
    def bar(self):
        return "bar from Base2"

class MyClass(Base1, Base2):
    pass

obj = MyClass()
print(obj.foo())  # Output: foo from Base1
print(obj.bar())  # Output: bar from Base2

#3.multilevel
#Ex:
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def drink_milk(self):
        print(f"{self.name} is drinking milk.")

class Cat(Mammal):
    def meow(self):
        print("Meow!")

# Create a Cat object and call its methods
cat = Cat("Whiskers")
cat.eat()        # Output: "Whiskers is eating."
cat.drink_milk() # Output: "Whiskers is drinking milk."
cat.meow()       # Output: "Meow!"

