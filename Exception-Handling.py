#!/usr/bin/env python
# coding: utf-8

# #1
# Exceptions: Exceptions are runtime errors that occur while the program is executing. They are usually caused by factors such as invalid inputs, resource unavailability, or logical errors in the program's logic. Exceptions can be handled and recovered from using exception handling mechanisms like try-except blocks.
# 
# Examples of exceptions include ValueError, TypeError, FileNotFoundError, IndexError, and ZeroDivisionError. These exceptions indicate various issues such as invalid values, incorrect types, missing files, index out of range, or division by zero.
# 
# Syntax Errors: Syntax errors, also known as parsing errors, occur during the parsing of the code, even before the program begins execution. They are caused by incorrect syntax or grammar in the code and prevent the program from running altogether. Syntax errors need to be fixed by correcting the code syntax.
# 
# Examples of syntax errors include missing colons, incorrect indentation, using undefined variables, or mismatched parentheses.

# #2
# '''if exception is not handled then program execution is terminated . for example if there are 100000 lines of code 
# in a program file and if there is a one line of code where error may occur that one line of code should be kept in try block 
# to execute other lines of code with out a problem.'''

# In[1]:


#3
'''try and except are the python statements used to handle the exception'''
#ex:
try:
    1/0
except Exception as e:
    print(e)


# In[2]:


#4
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Result:", result)
        return result
    finally:
        print("Division operation complete.")

divide_numbers(10, 2)  # Case 1: Division successful
print()
divide_numbers(10, 0)  # Case 2: Division by zero

#else is executed when there is no error in try block and finally is alway executed 


# In[3]:


#5
#In Python, custom exceptions are user-defined exception classes that inherit from the built-in Exception class or its subclasses. Custom exceptions allow developers to define their own specific exception types tailored to their application's needs. They provide a way to handle and communicate application-specific errors or exceptional conditions that may occur during the execution of a program.

class InsufficientBalanceError(Exception):
    def __init__(self, account_number):
        self.account_number = account_number

    def __str__(self):
        return f"Insufficient balance in account {self.account_number}"


def withdraw_from_account(account_number, amount, balance):
    try:
        if amount > balance:
            raise InsufficientBalanceError(account_number)
        else:
            # Withdraw the amount
            pass
    except InsufficientBalanceError as e:
        print("Error:", str(e))


withdraw_from_account("A1234", 5000, 3000)


# In[4]:


#6 custom exception checks if number ebtered is odd or even . if it is odd then exception is raised

class even(Exception):
    def __init__(self,msg):
        self.msg=msg
        
def even_fun(num):
    if num%2!=0:
        raise even("not entered even number")
    else:
        print("even ")
try:
    num=int(input("enter even number:"))
    even_fun(num)
except Exception as e:
    print(e)
    


# In[ ]:





# In[ ]:




