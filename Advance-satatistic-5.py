#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1
import numpy as np
from scipy.stats import norm

mean=50
sample_size=100
std=5
alpha=0.05

critical_value=norm.ppf(1-(alpha/2))

standard_error= std/np.sqrt(sample_size)

margin_error= critical_value*standard_error

confidence_interval=(mean-margin_error,mean+margin_error)

print("Confidence Interval:", confidence_interval)


# In[9]:


#2
import numpy as np
import scipy.stats as stat


observed = [35, 40, 20, 10, 15, 20]  # Observed counts of each color
expected = [0.2, 0.2, 0.2, 0.1, 0.1, 0.2]

total=sum(observed)
expected_counts=[i*total for i in expected]

chi_stat,p_value=stat.chisquare(observed,expected_counts)

alpha=0.05
dof=len(observed)-1

critical_value= stat.chi2.ppf(1-alpha,dof)


# In[11]:


if chi_stat>critical_value:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# #3
# Outcome 1 20 15
# Outcome 2 10 25
# Outcome 3 15 20

# In[15]:


import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([[20, 15],
                    [10, 25],
                    [15, 20]])

# Calculate expected frequencies under the assumption of independence
row_totals = np.sum(observed, axis=1)
print(row_totals)
col_totals = np.sum(observed, axis=0)
print(col_totals)
total = np.sum(row_totals)
expected = np.outer(row_totals, col_totals) / total

# Perform chi-square test
chi2_stat, p_value, _, _ = chi2_contingency(observed)

print("Observed frequencies:")
print(observed)
print("Expected frequencies:")
print(expected)
print("Chi-square statistic:", chi2_stat)
print("P-value:", p_value)


# In[16]:


#4
import numpy as np
from scipy.stats import norm
mean=60
n=500
alpha=0.05
proportion=mean/n

standard_error=np.sqrt((proportion)*(1-proportion)/n)

critical_value=norm.ppf(1-alpha)

margin_error=standard_error*critical_value

confidence_interval=(mean-margin_error,mean+margin_error)


# In[17]:


print(confidence_interval)


# In[18]:


#we are 95% confidence that true population mean who smokes fall with in this region 


# In[19]:


#5

import numpy as np
from scipy.stats import norm

mean=75
sample_size=100
std=12
alpha=0.1

critical_value=norm.ppf(1-(alpha/2))

standard_error= std/np.sqrt(sample_size)

margin_error= critical_value*standard_error

confidence_interval=(mean-margin_error,mean+margin_error)

print("Confidence Interval:", confidence_interval)


# In[30]:


#6
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat

dof=10
chi_sqare_stat=15

df=10

x=np.linspace(0,30,1000)
print(x)

y=stat.chi2.pdf(x,df)
print(y)


# In[31]:


plt.plot(x,y,label="dof=10")


# In[33]:


x_shade = np.linspace(15, 30, 100)
y_shade = stat.chi2.pdf(x_shade, df)
plt.fill_between(x_shade, y_shade, alpha=0.3)

# Label the axes
plt.xlabel('Chi-square Statistic')
plt.ylabel('Probability Density Function')

# Set the plot title
plt.title('Chi-square Distribution')

# Show the legend
plt.legend()

# Display the plot
plt.show()


# In[36]:


#8
import numpy as np
import scipy.stats as stat

observed=[45,55]
expected=[50,50]

dof=len(observed)-1

chi_stat,p_value=stat.chisquare(observed,expected)

critical_value=stat.chi2.ppf(1-0.05,dof)

if chi_stat>critical_value:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[37]:


#9

import numpy as np
from scipy.stats import chi2_contingency

# Create the contingency table
observed = np.array([[60, 140], [30, 170]])

# Perform chi-square test for independence
chi2, p_value, dof, expected = chi2_contingency(observed)

# Set the significance level
alpha = 0.05

# Compare the p-value with the significance level to make the decision
if p_value < alpha:
    print("Reject the null hypothesis, there is a significant association between smoking status and lung cancer diagnosis.")
else:
    print("Fail to reject the null hypothesis, there is no significant association between smoking status and lung cancer diagnosis.")


# In[43]:


import numpy as np
import scipy.stats as stat


observed=np.array([200,150,150])

chi_stat,p_value,dof,expected= stat.chi2_contingency(observed)

critical_value=stat.chi2.ppf(1-0.01,dof)
alpha=0.01
if p_value < alpha:
    print("Reject the null hypothesis, there is a significant association between chocolate preference and country of origin.")
else:
    print("Fail to reject the null hypothesis, there is no significant association between chocolate preference and country of origin.")

if chi_stat>critical_value:
    print("reject null hypothesis")
else:
    print("accept null hyppothesis")


# In[45]:


#11
import numpy as np
from scipy.stats import t

sample_mean = 72
sample_size = 30
sample_std = 10
population_mean = 70

# Calculate the t-statistic
t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))

# Calculate the degrees of freedom
degrees_of_freedom = sample_size - 1

# Set the significance level
alpha = 0.05

# Calculate the critical value
critical_value = t.ppf(1 - alpha / 2, degrees_of_freedom)

# Calculate the p-value
p_value = 2 * (1 - t.cdf(abs(t_statistic), degrees_of_freedom))

# Make the decision
if p_value < alpha:
    decision = "Reject the null hypothesis"
else:
    decision = "Fail to reject the null hypothesis"

# Print the results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
print("Decision:", decision)


# In[ ]:




