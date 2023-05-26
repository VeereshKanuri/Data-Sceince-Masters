#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#1
pd.Series([4, 8, 15, 16, 23,42])


# In[4]:


#2
list1=["veeresh",1,2,3,4,5,6,"sai","rishi","hello"]
pd.Series(list1)


# In[5]:


#3
data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
pd.DataFrame(data)


# #4
# 
# 
# DataFrame: The DataFrame is a two-dimensional tabular data structure in Pandas that consists of rows and columns. It is similar to a spreadsheet or a SQL table and provides powerful indexing, slicing, reshaping, and merging capabilities.
# 
# Series: A Series is a one-dimensional labeled array that can hold any data type. It is often used to represent a single column or row of data in a DataFrame.
# ex:
# data = {
#     'Name': ['Alice', 'Bob', 'Claire'],
#     'Age': [25, 30, 27],
#     'Gender': ['Female', 'Male', 'Female']
# }
# pd.DataFrame(data)
# 
# ex2:
# list1=["veeresh",1,2,3,4,5,6,"sai","rishi","hello"]
# pd.Series(list1)

# #5
# 
# head() and tail(): These functions allow you to view the first or last n rows of the DataFrame. They are useful for quickly inspecting the structure and content of the DataFrame.
# 
# info(): This function provides a concise summary of the DataFrame, including the data types, column names, and non-null counts. It is helpful for understanding the overall structure of the DataFrame.
# 
# describe(): This function generates descriptive statistics of the numerical columns in the DataFrame, such as count, mean, standard deviation, minimum, maximum, and quartile values. It provides a quick overview of the distribution of the data.
# 
# shape: This attribute returns a tuple representing the dimensions of the DataFrame (number of rows, number of columns). It is useful for getting the size of the DataFrame.
# 
# isnull() and notnull(): These functions return a DataFrame of the same shape as the input, indicating whether each element is missing (NaN) or not. They are used to identify missing values in the DataFrame.
# 

# #6
# 
# Series: A Series is a one-dimensional labeled array in Pandas that can hold data of any type. It is mutable, which means you can modify its values after creation. You can change the values of individual elements in a Series by assigning new values to them or using 
# 
# DataFrame: A DataFrame is a two-dimensional tabular data structure in Pandas, consisting of rows and columns. It is also mutable, allowing you to modify its values, add or remove columns, and perform various data manipulation operations.
# 
# Panel: Panel structure in Pandas is indeed mutable, meaning you can modify its values and structure

# In[8]:


#7

series1=pd.Series(["veeresh","sai","vinay"])
series2=pd.Series([21,23,10])
series3=pd.Series(["brother","elder_brother","younger_brother"])

df=pd.DataFrame({"name":series1,"age":series2,"relation":series3})
df

