#!/usr/bin/env python
# coding: utf-8

# #1
# 
# Estimation statistics is a branch of statistics that focuses on estimating population parameters based on sample data. It involves using sample statistics to make inferences and draw conclusions about the unknown population parameters. Two common types of estimation in statistics are point estimation and interval estimation.
# 
# 1. Point Estimate: A point estimate is a single value that serves as an estimate or best guess of an unknown population parameter. It is obtained by using a sample statistic that is calculated from the sample data. For example, if we want to estimate the population mean, we can use the sample mean as a point estimate. Similarly, if we want to estimate the population proportion, we can use the sample proportion as a point estimate. Point estimates provide a concise summary of the estimated parameter, but they do not provide any information about the uncertainty or variability associated with the estimate.
# 
# 2. Interval Estimate: An interval estimate provides a range of values within which the true population parameter is likely to fall. It takes into account the uncertainty and variability in the estimate. The interval estimate is constructed by specifying a margin of error or a level of confidence. The margin of error reflects the precision of the estimate, while the level of confidence represents the degree of confidence we have in capturing the true parameter within the interval. Commonly used levels of confidence are 90%, 95%, and 99%. The interval estimate is typically presented as a range of values with an associated confidence level. For example, we might estimate the population mean to be 95% confident that it falls within the interval [45, 55]. This means that if we repeated the sampling process and constructed intervals in the same way, approximately 95% of those intervals would capture the true population mean.
# 
# Interval estimates provide more information compared to point estimates as they quantify the uncertainty associated with the estimate. They allow us to express the precision and reliability of the estimate and provide a range of plausible values for the population parameter.
# 
# Both point estimates and interval estimates are used in estimation statistics to make inferences and draw conclusions about population parameters based on sample data. The choice between using a point estimate or an interval estimate depends on the specific research question, the desired level of precision and confidence, and the trade-off between simplicity and capturing uncertainty.

# In[1]:


#2

def estimate_population_mean(sample_mean, sample_std_dev, sample_size):
    # Calculate the standard error
    standard_error = sample_std_dev / (sample_size ** 0.5)
    
    # Calculate the margin of error (assuming a 95% confidence level)
    margin_of_error = 1.96 * standard_error
    
    # Calculate the lower and upper bounds of the confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    
    # Return the estimated population mean and the confidence interval
    return sample_mean, lower_bound, upper_bound


# #3
# Hypothesis testing is a statistical method used to make inferences or draw conclusions about a population based on a sample of data. It involves formulating two competing hypotheses, the null hypothesis (H0) and the alternative hypothesis (Ha), and analyzing the sample data to determine which hypothesis is more likely to be true.
# 
# The main purpose of hypothesis testing is to provide a systematic framework for making decisions and drawing conclusions in the face of uncertainty. It helps researchers and analysts evaluate the validity of claims or assumptions, test research hypotheses, and make informed decisions based on the available evidence.

# #4
# 
# Null Hypothesis (H0): The average weight of male college students is equal to or less than the average weight of female college students.
# 
# Alternative Hypothesis (Ha): The average weight of male college students is greater than the average weight of female college students.

# In[12]:


import numpy as np 
from scipy.stats import norm


# In[13]:


def two_test(sample1,sample2,alpha):
    n1=len(sample1)
    n2=len(sample2)
    mean1=np.mean(sample1)
    mean2=np.mean(sample2)
    var1=np.var(sample1,ddof=1)
    var2=np.var(sample2,ddof=1)
    
    pooled_std = np.sqrt((var1/n1) + (var2/n2))

    # Calculate the z-score
    z_score = (mean1 - mean2) / pooled_std
    print(z_score)

    # Calculate the critical value based on the alpha level
    crit_val = norm.ppf(1 - alpha/2)
    print(crit_val)

    # Calculate the p-value
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    print(p_value)

    # Compare the z-score with the critical value to make the decision
    if abs(z_score) > crit_val:
        decision = "Reject the null hypothesis"
    else:
        decision = "Fail to reject the null hypothesis"

    return z_score, p_value, decision


# In[14]:


sample1 = [73, 68, 72, 65, 70]
sample2 = [68, 66, 70, 72, 67]
alpha = 0.05

z_score, p_value, decision = two_test(sample1, sample2, alpha)

print("Z-Score:", z_score)
print("P-Value:", p_value)
print("Decision:", decision)


# #5
# 
# null hypothesis and alternative hypothesis are two opposite statements about population parameter.
# null hypothesis assumes that there is no significant difference or effects observed
# alternatives hypothesis assumes that there is significant difference or effects observed.
# 
# for examples : there are different houses in an area with different heights and its assumed that mean of heights is 160cm . but one guy doubted and took sample of 40 houses and calculated mean of height and found that its 164cm.
# 
# HYPOTHESIS TESTING
# NULL HYPOTHESIS : there is no change in mean
# ALTERNATIVE HYPOTHESIS : there is change in mean

# In[ ]:


#6

1. state the hypothesis
2. set the significance value
3. choose appropiate statistic method
4. determine z-score ot t-score
5. compute p- value
6. compare p-value with significance value 
    if p-value > significance then null hypothesis : fail to reject null hypothesis
    if p-value < significance then : reject null hypothesis


# #7
# 
# In simple terms, the p-value is a measure that tells us how likely we would observe the data we have collected if the null hypothesis were true. It helps us decide whether the evidence we have gathered supports or contradicts the null hypothesis

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Set the degrees of freedom
df = 10

# Generate x values from -4 to 4
x = np.linspace(-4, 4, 100)
print(x)
# Calculate the corresponding y values using the t-distribution PDF
y = t.pdf(x, df)
print(y)

# Plot the t-distribution
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title(f"Student's t-distribution (df={df})")
plt.grid(True)
plt.show()


# In[22]:


import numpy as np
from scipy.stats import t
import math


# In[34]:


def two_sample(sample1,sample2):
    n1=len(sample1)
    n2=len(sample2)
    mean1=np.mean(sample1)
    mean2=np.mean(sample2)
    var1=np.var(sample1)
    var2=np.var(sample2)
    
    std=math.sqrt((var1)/n1 + (var2)/n2)
    
    #t-score
    t_score= (mean1-mean2)/std
    #dof
    dof=n1+n2-2
    
    #p-value
    
    p_value=2*(1-t.cdf(abs(t_score),dof))
    
    if abs(t_score) <p_value:
        decision = "Reject the null hypothesis"
    else:
        decision = "Fail to reject the null hypothesis"

    return t_score, p_value,decision    


# In[35]:


sample1 = np.array([25, 30, 28, 32, 35])
sample2 = np.array([20, 26, 24, 29, 31])

t_score, p_value, decision = two_sample(sample1, sample2)

print("T-Score:", t_score)
print("P-Value:", p_value)
print("Decision:", decision)


# #11
# The Student's t-distribution, also known as the t-distribution, is a probability distribution that is used in statistical inference when working with small sample sizes or when the population standard deviation is unknown

# #12
# The t-statistic, also known as the student's t-statistic, is a measure of how the sample mean differs from the hypothesized population mean, relative to the variability in the sample. It is used in hypothesis testing to assess whether there is a significant difference between the sample mean and the hypothesized population mean.
# 
# The formula for calculating the t-statistic is as follows:
# 
# t = (sample_mean - hypothesized_mean) / (sample_standard_deviation / sqrt(sample_size))

# In[36]:


#13
import math

sample_mean = 500
standard_deviation = 50
sample_size = 50
confidence_level = 0.95

critical_value = 1.96 #from z-table
standard_error = standard_deviation / math.sqrt(sample_size)
margin_of_error = critical_value * standard_error

lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

confidence_interval = (lower_bound, upper_bound)

print("Confidence Interval:", confidence_interval)


# In[40]:


#14
import numpy as np
from scipy.stats import norm
import math

population_mean=10
sample_mean=8
std_dev=3
sample_size=100

#z-score

z_score= (sample_mean-population_mean)/(std_dev/math.sqrt(sample_size))

#p_value

p_value = norm.cdf(z_score)

#alpha
alpha=0.05

#condition

if p_value> alpha:
    decision="accept null hypothesis"
else:
    decision="reject null hypothesis"



# In[41]:


# Print the results
print("Z-Score:", z_score)
print("P-Value:", p_value)
print("Decision:", decision)


# In[42]:


#15

import numpy as np
from scipy.stats import norm
import math

population_mean=5
sample_mean=4.8
std_dev=0.5
sample_size=25

#z-score

z_score= (sample_mean-population_mean)/(std_dev/math.sqrt(sample_size))

#p_value

p_value = norm.cdf(z_score)

#alpha
alpha=0.01

#condition

if p_value<alpha:
    decision="reject null hypothesis"
else:
    decision="fail to reject null hypothesis"


# In[43]:


# Print the results
print("Z-Score:", z_score)
print("P-Value:", p_value)
print("Decision:", decision)


# Since the p-value is greater than the significance level of 0.01, we accept the null hypothesis and conclude that there is evidence to support the claim that the true mean weight of the products is not less than 5 pounds.
# 
# 

# In[45]:


#16

import numpy as np
from scipy.stats import norm

n1 = 30
sample_mean1 = 80
std1 = 10

n2 = 40
sample_mean2 = 75
std2 = 8

# Calculate the pooled standard deviation
pooled_std = np.sqrt(((std1**2 / n1) + (std2**2 / n2)))

# Calculate the z-score
z_score = (sample_mean1 - sample_mean2) / pooled_std

# Calculate the p-value
p_value = 2 * (1 - norm.cdf(abs(z_score)))

# Set the significance level (alpha)
alpha = 0.01

# Make the decision
if p_value < alpha:
    decision = "Reject the null hypothesis"
else:
    decision = "Fail to reject the null hypothesis"

# Print the results
print("Z-Statistic:", z_score)
print("P-Value:", p_value)
print("Decision:", decision)


# In[48]:


#17
import math

sample_mean = 4
standard_deviation = 1.5
sample_size = 50
confidence_level = 0.99

critical_value = 2.58 #from z-table
standard_error = standard_deviation / math.sqrt(sample_size)
margin_of_error = critical_value * standard_error

lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

confidence_interval = (lower_bound, upper_bound)

print("Confidence Interval:", confidence_interval)


# The 99% confidence interval for the average number of ads watched by viewers during a TV program is approximately (3.68, 4.32). This means that we are 99% confident that the true population mean falls within this interval.
