#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import numpy as np
import scipy.stats as stat
def f_test(arr1,arr2):
    var1=np.var(arr1)
    var2=np.var(arr2)
    F=var1/var2
    
    dof1=len(arr1)-1
    dof2= len(arr2)-1
    
    p_value=1-(stat.f.cdf(F,dof1,dof2))
    
    
    return F,p_value
    
    
    


# In[2]:


#2

def fun(alpha,df1,df2):
    
    return stat.f.ppf(1-alpha/2,df1,df2)


# In[3]:


#3
import numpy as np

def fun():
    
    sample1= np.random.normal(loc=0,scale=1,size=100)
    sample2=np.random.normal(loc=0,scale=1.5,size=100)
    
    var1=np.var(sample1)
    var2=np.var(sample2)
    
    F_test= var1/var2
    
    dof1=len(sample1)-1
    dof2=len(sample2)-1
    
    p_value=1-(stat.f.cdf(F_test,df1,df2))
    
    return F_value,dof1,dof2,p_value


# In[5]:


#4

#null hypothesis : varainces are not significantly different
#alternative hypothesis : varainces are significantly different

alpha=0.05

var1=10
var2=15

dof1=11
dof2=11

f_value= var1/var2

p_value=1-stat.f.cdf(f_value,dof1,dof2)

critical_value= stat.f.ppf(1-alpha,dof1,dof2)

if f_value>critical_value:
    print("reject null hypothesis")
    print("The variances are significantly different.")
else:
    print("fail to reject null hypothesis")
    print("The variances are not significantly different.")


# In[6]:


#5

from scipy.stats import f

# Claimed variance
claimed_variance = 0.005

# Sample variance
sample_variance = 0.006

# Sample size
n = 25

# Degrees of freedom
df1 = n - 1
df2 = n - 1

# Calculate the F-statistic
f_value = sample_variance / claimed_variance

# Calculate the critical F-value
alpha = 0.01  # Significance level
critical_f_value = f.ppf(1 - alpha, df1, df2)

# Compare the F-statistic with the critical F-value
if f_value > critical_f_value:
    print("Reject the null hypothesis.")
    print("The claim is not justified.")
else:
    print("Fail to reject the null hypothesis.")
    print("The claim is justified.")


# In[7]:


#6

n1=10
var1=25

n2=15
var2=20

dof1=n1-1
dof2=n2-1

f_value= var1/var2

alpha=0.1

critical_value=stat.f.ppf(1-alpha,dof1,dof2)

if f_value > critical_f_value:
    print("Reject the null hypothesis.")
    print("The claim is not justified.")
else:
    print("Fail to reject the null hypothesis.")
    print("The claim is justified.")


# In[8]:


#7

import numpy as np
from scipy import stats

sample_a = [24, 25, 28, 23, 22, 20, 27]
sample_b = [31, 33, 35, 30, 32, 36]

variance_a = np.var(sample_a, ddof=1)
variance_b = np.var(sample_b, ddof=1)


f_statistic = variance_a / variance_b

degrees_of_freedom_numerator = len(sample_a) - 1
degrees_of_freedom_denominator = len(sample_b) - 1

alpha = 0.05
critical_value = stats.f.ppf(1 - alpha, degrees_of_freedom_numerator, degrees_of_freedom_denominator)

if f_statistic > critical_value:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")


# In[10]:


#8

import numpy as np
from scipy import stats

group_a = [80, 85, 90, 92, 87, 83]
group_b = [75, 78, 82, 79, 81, 84]

variance_a = np.var(group_a, ddof=1)
variance_b = np.var(group_b, ddof=1)

f_statistic = variance_a / variance_b

degrees_of_freedom_numerator = len(group_a) - 1
degrees_of_freedom_denominator = len(group_b) - 1

alpha = 0.01
critical_value = stats.f.ppf(1 - alpha, degrees_of_freedom_numerator, degrees_of_freedom_denominator)

if f_statistic > critical_value:
    print("The variances are significantly different.")
else:
    print("The variances are not significantly different.")


# In[ ]:




