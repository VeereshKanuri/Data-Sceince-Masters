#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list_ = [ '1','2','3','4','5']
array_list = np.array(object = list_)


# #1
# Yes, there is a difference in the data type of the variables list_ and array_list. The list_ variable is a Python list, while the array_list variable is a NumPy array.
# list_ = ['1', '2', '3', '4', '5']
# array_list = np.array(list_)
# 
# print(type(list_))       # Output: <class 'list'>
# print(type(array_list))  # Output: <class 'numpy.ndarray'>

# In[5]:


#2
for i in list_:
    print(type(i))


# In[7]:


for i in array_list:
    print(type(i))


# In[8]:


#3
array_list = np.array(object = list_, dtype = int)


# In[9]:


for i in list_:
    print(type(i))


# In[10]:


for i in array_list:
    print(type(i))


# In[11]:


num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)


# In[13]:


np.shape(num_array)


# In[14]:


np.size(num_array)


# In[16]:


#5
arr1=np.zeros((3,3))
arr1


# In[19]:


#6
arr2=np.eye(5,5)
arr2


# In[ ]:




