#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
def fun(l):
    lis2=[]
    sum=1
    for i in list1:
        if type(i)==int:
            sum=sum*i
        if type(i)==list:
            for j in i:
                if type(j)==int:
                    sum=sum*j
        if type(i)==tuple:
            for k in i:
                if type(k)==int:
                    sum=sum*k
        if type(i)==set:
            for l in i:
                if type(l)==int:
                    sum=sum*l
        if type(i)==dict:
            for m in i.keys():
                if type(m)==int:
                    sum=sum*m
            for n in i.values():
                if type(n)==int:
                    sum=sum*n
    return sum
        
            


# In[2]:


fun(list1)


# In[3]:


#2
def encrypt_message(message):
    encrypted = ""
    for char in message:
        if char == " ":
            encrypted += "$"
        elif char.isalpha():
            encrypted += chr(219 - ord(char))
        else:
            encrypted += char
    return encrypted

# Example usage
input_sentence = "I want to become a Data Scientist."
encrypted_sentence = encrypt_message(input_sentence)
print(encrypted_sentence)


# In[ ]:




