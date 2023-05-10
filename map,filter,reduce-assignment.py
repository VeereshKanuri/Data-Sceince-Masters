#!/usr/bin/env python
# coding: utf-8

# #1
# l1=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
# lst = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
# 
# sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
# 
# print(sorted_lst)
# 
# #output
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
# 

# In[1]:


#2
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x:x**2,l))


# In[3]:


#3
l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple(map(lambda x:str(x),l))


# In[6]:


#4
from functools import reduce
lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
reduce(lambda x,y:x*y,lis)


# In[8]:


#5
l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x%2==0 and x%3==0,l))


# In[12]:


#6
a=['python', 'php', 'aba', 'radar', 'level']
list(filter(lambda x:x==x[::-1],a))


# In[ ]:




