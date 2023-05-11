#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=input("enter password")
def fun(x):
    sum1=0
    count=0
    num=0
    special_count=0
    if len(x)!=10:
        print("password is invalid")
    for i in x:
        if i.isupper()==True:
            sum1=sum1+1
            
        if i.islower()==True:
            count=count+1
        
        if i.isdigit()==True:
            num=num+1
        if i in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            special_count += 1
    if sum1>=2 and count>=2 and num>=1 and special_count>=3:
        print("password is correct")
    else:
        print("password is incorrect")
    
        
fun(x)       
    


# In[14]:


#2
#square of numbers 1 to 10
list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10]))
#cube root
list(map(lambda x:x**(1/3),[1,2,3,4,5,6,7,8,9,10]))
#even check
X=lambda x:x%2==0
print(X(2))
#filter oddnumbers 
l=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2!=0,l))
#Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
#string starts with particular letter
string = "Python"
starts_with_p = lambda s: s.startswith("P")
print(starts_with_p(string))
#string is numeric
s=lambda x: x.isnumeric()
#sorting list of tuples
#Sort a list of tuples having fruit names and their quantity. 
l=[("mango",99),("orange",80), ("grapes", 1000)]
sorted(l,key=lambda x:x[1])


# In[13]:





# In[ ]:





# In[ ]:




