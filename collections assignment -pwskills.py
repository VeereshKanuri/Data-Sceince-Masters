#!/usr/bin/env python
# coding: utf-8

# #1
# Yes, a tuple is immutable in Python. Once a tuple is created, you cannot modify its contents.
# 
# Here are some characteristics of tuples in Python:
# 
# Tuples are ordered: The elements in a tuple are ordered, meaning they have a specific position/index in the tuple.
# Tuples are indexed: You can access elements in a tuple using their index, starting from 0 for the first element.
# Tuples are immutable: Once a tuple is created, you cannot modify its contents. This means you cannot add, remove, or modify elements in a tuple.
# Tuples can contain any type of object: You can have tuples containing elements of different types, such as integers, floats, strings, and other objects.
# Tuples can be nested: You can have tuples containing other tuples, or other data types like lists or dictionaries.
# Tuples are often used in Python to represent a collection of related values that should not be modified. For example, you might use a tuple to represent a point in 2D space with the x and y coordinates as its elements:

# #2
# The two tuple methods in Python are count() and index().
# example 1:
# tup = (1, 2, 3, 4, 2, 2)
# count_2 = tup.count(2)
# print(count_2) # Output: 3
# In the above example, the count() method is used to count the number of times the element 2 appears in the tuple tup. The output will be 3, since 2 appears three times in the tuple.
# example 2:
# tup = (1, 2, 3, 4, 2, 2)
# index_2 = tup.index(2)
# print(index_2) # Output: 1
# In the above example, the index() method is used to find the index of the first occurrence of the element 2 in the tuple tup. The output will be 1, since 2 appears at index 1 in the tuple.
# 
# Tuples have only two in-built methods, count() and index(), because they are immutable, which means that their elements cannot be modified once they are created. Lists, on the other hand, have more in-built methods because they are mutable, meaning that their elements can be modified after they are created. The additional methods in lists allow for more flexibility in modifying and manipulating their contents.
# 
# 

# #3
# In Python, the collection datatype that does not allow duplicate items is the sets and dictionaries.
# 
# Here is the code to remove duplicates from the given list using a set:
# lst = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
# 
# lst_set = set(lst) # convert the list to a set
# lst_no_duplicates = list(lst_set) # convert the set back to a list
# 
# print(lst_no_duplicates)
# 
# output=[1, 2, 3, 4]
# 
# 

# #4
# Both the union() and update() methods are used to combine two or more sets into a single set. However, there are some differences between the two methods:
# 
# The union() method returns a new set containing all the distinct elements from all the sets being combined, without modifying the original sets.
# The update() method modifies the original set by adding all the elements from another set (or multiple sets) to it. If the set being added already contains some of the elements in the original set, they are not duplicated.
# Here are examples of both methods:
#     # Example of union() method
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {5, 6, 7}
# 
# new_set = set1.union(set2, set3)
# 
# print(new_set) # output: {1, 2, 3, 4, 5, 6, 7}
# print(set1)    # output: {1, 2, 3}
# 
# # Example of update() method
# set4 = {7, 8, 9}
# 
# set1.update(set4)
# 
# print(set1) # output: {1, 2, 3, 7, 8, 9}
# 

# #5
# In Python, a dictionary is a collection of key-value pairs, where each key is associated with a corresponding value. It is represented by {} (curly braces) and each key-value pair is separated by a comma. The keys must be unique and immutable (strings, integers, or tuples), while the values can be of any type.
# 
# Here's an example of a dictionary:
# person = {'name': 'John', 'age': 32, 'city': 'New York'}
# 
# print(person['name']) # output: 'John'
# print(person['age'])  # output: 32
# print(person['city']) # output: 'New York'
# 
# In this example, we have a dictionary person with three key-value pairs. The keys are 'name', 'age', and 'city', and the corresponding values are 'John', 32, and 'New York'. We can access the values in the dictionary by using the key in square brackets.
# 
# A dictionary in Python is unordered, which means that the order in which the key-value pairs are stored in the dictionary is not fixed. The keys and values are stored in a way that allows for fast retrieval, but not necessarily in the order in which they were added. However, starting from Python 3.7, the order of insertion is preserved.
# 

# #6
# Yes, we can create a nested dictionary in Python. A nested dictionary is a dictionary that contains another dictionary as its value.
# 
# Here's an example of a simple one-level nested dictionary:
# car = {'make': 'Toyota', 
#        'model': 'Corolla', 
#        'year': 2021, 
#        'specs': {'engine': '1.8L', 
#                  'transmission': 'CVT', 
#                  'color': 'silver'}
#       }
# In this example, we have a dictionary car with four key-value pairs. The first three key-value pairs ('make', 'model', and 'year') are simple key-value pairs with string and integer values. The fourth key-value pair ('specs') has a dictionary as its value. The dictionary 'specs' contains three key-value pairs ('engine', 'transmission', and 'color') that describe the specifications of the car.
# 
# We can access the nested dictionary by using the key of the outer dictionary to access the inner dictionary and then using the key of the inner dictionary to access its value. For example, to get the color of the car, we can use the following code.
# color = car['specs']['color']
# print(color) # output: 'silver'
# 

# #7
# To create a new key-value pair using the setdefault() method, we can provide the key and the default value for the key if it doesn't already exist in the dictionary. If the key already exists in the dictionary, the method returns the current value of the key without modifying the dictionary.
# 
# Here's an example of how to use the setdefault() method to create a new key 'topics' and set its value to ['Python', 'Machine Learning', 'Deep Learning']:
# dict1 = {'language': 'Python', 'course': 'Data Science Masters'}
# 
# # using setdefault method to create a new key 'topics' and set its value
# dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])
# 
# # printing the updated dictionary
# print(dict1)
# output
# {'language': 'Python', 'course': 'Data Science Masters', 'topics': ['Python', 'Machine Learning', 'Deep Learning']}
# In the above example, we first define a dictionary dict1 with two key-value pairs. We then use the setdefault() method to create a new key 'topics' and set its value to ['Python', 'Machine Learning', 'Deep Learning']. Since the key 'topics' does not exist in the dictionary, the method adds it as a new key-value pair. Finally, we print the updated dictionary to confirm that the key 'topics' has been added with the given value.
# 
# Note that the setdefault() method is particularly useful when we want to add a new key-value pair to a dictionary, but we're not sure whether the key already exists in the dictionary or not. The method provides a simple and concise way to add a new key-value pair to a dictionary without having to write additional code to check for the existence of the key.

# In[ ]:


#8
The three view objects in dictionaries are:

dict.keys() : This method returns a view object of all the keys in the dictionary.
dict.values() : This method returns a view object of all the values in the dictionary.
dict.items() : This method returns a view object of all the key-value pairs in the dictionary.
Here's an example code to display these view objects for the given dictionary:
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}

# Displaying keys view object
print(dict1.keys())

# Displaying values view object
print(dict1.values())

# Displaying items view object
print(dict1.items())
#output
dict_keys(['name', 'age', 'city'])
dict_values(['John', 30, 'New York'])
dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# Creating view objects
keys_view = dict1.keys()
values_view = dict1.values()
items_view = dict1.items()

# Displaying view objects
print("Keys view object:", keys_view)
print("Values view object:", values_view)
print("Items view object:", items_view)
#output
Keys view object: dict_keys(['Sport', 'Teams'])
Values view object: dict_values(['Cricket', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']])
Items view object: dict_items([('Sport', 'Cricket'), ('Teams', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand'])])

