#!/usr/bin/env python
# coding: utf-8

# #1
# One important reason for using the Exception class as the base class for custom exceptions is compatibility with the existing exception handling system in Python.
# 
# Python has a built-in exception hierarchy, with the base Exception class at the top. By inheriting from Exception, our custom exception becomes part of this hierarchy, allowing it to be caught and handled using the same exception handling mechanisms that work with built-in exceptions.
# 
# When we raise an exception using raise and catch it with a try-except block, the except block specifies the type of exception to catch. By inheriting from Exception, our custom exception can be caught in a generic except Exception block, which handles exceptions of any type derived from Exception. This provides a convenient way to handle multiple types of exceptions in a consistent manner.

# In[ ]:


#3
#The ArithmeticError class is a base class for exceptions that occur during arithmetic operations in Python. It is a subclass of the Exception class and provides a hierarchy of exceptions related to arithmetic errors.

#Two examples of errors defined in the ArithmeticError class are:

#ZeroDivisionError: This exception is raised when division or modulo operation is performed with zero as the divisor.
#ex:
    try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")


#OverflowError: This exception is raised when the result of an arithmetic operation is too large to be represented within the available memory.

#ex :
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")


# In[1]:


#4
##The LookupError class in Python is a base class for exceptions that occur when a lookup or indexing operation fails. It serves as a superclass for more specific lookup-related exceptions like KeyError and IndexError.

##Here's an explanation of KeyError and IndexError and how they relate to the LookupError class:

##KeyError: This exception is raised when a dictionary key or a set element is not found during a lookup operation.
my_dict = {'name': 'John', 'age': 25}

try:
    value = my_dict['address']
except KeyError:
    print("Error: Key not found in dictionary!")


##IndexError: This exception is raised when an index used for list, tuple, or string access is out of range or not found.
my_list = [1, 2, 3]

try:
    value = my_list[5]
except IndexError:
    print("Error: Index out of range!")


# # 5
# import veeresh
# 
# ModuleNotFoundError                       Traceback (most recent call last)
# ~\AppData\Local\Temp\ipykernel_8908\2108618437.py in <module>
# ----> 1 import veeresh #module not found error
# 
# ModuleNotFoundError: No module named 'veeresh'

# #6
# try:
#     1/0                           #not a good way of practice
# except Exception as e:
#     print(e)
#     
#  try:
#     1/0                          #good way of practice
# except ZeroDivisionError as e:
#     print(e)
#     
#     
# #always try to log than print
# 
# import logging
# logging.basicConfig(filename='error.log',level=logging.ERROR)
# try:
#     10/0
# except ZeroDivisionError as e:
#     logging.error("the error is  {}".format(e))
# 
# #clean up all resources 
# 
# try:
#     file=open('text.txt','w')
#     file.write("hello")
# except FileNotFoundError as e:
#     print(e)
# finally:
#     file.close()
