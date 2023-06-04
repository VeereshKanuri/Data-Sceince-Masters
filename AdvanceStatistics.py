#!/usr/bin/env python
# coding: utf-8

# #1
# 
# The probability density function (PDF) is a fundamental concept in probability theory and statistics. It is a mathematical function that describes the likelihood of a continuous random variable taking on a particular value or falling within a range of values.
# 
# In simpler terms, the PDF provides a way to describe the probability distribution of a continuous random variable. It gives an indication of the relative likelihood of observing different values of the variable.
# 
# Continuous Random Variables: The PDF is used to describe continuous random variables, which are variables that can take on any value within a certain range or interval. Examples of continuous random variables include height, weight, temperature, and time.
# 
# Probability Density: The PDF represents the probability density, rather than the actual probability. The probability of a continuous random variable taking on a specific value is zero since there are infinitely many possible values. Instead, the PDF measures the likelihood of the variable falling within a range of values.

# #2
# 
# Continuous Probability Distributions:
# 
# Normal Distribution: Also known as the Gaussian distribution, it is a symmetric bell-shaped distribution characterized by its mean and standard deviation. It is widely used due to its applicability to many natural phenomena.
# 
# Uniform Distribution: Represents a constant probability for a continuous random variable over a specified interval.
# 
# Discrete Probability Distributions:
# 
# Bernoulli Distribution: Represents the probability of success or failure for a single binary outcome.
# Binomial Distribution: Describes the probability of obtaining a specific number of successes in a fixed number of independent Bernoulli trials.
# 
# Poisson Distribution: Models the probability of a given number of events occurring in a fixed interval of time or space, assuming a constant average rate of occurrence.

# In[3]:


#3

import math

def normal_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    exponent = -((x - mean) ** 2) / (2 * std_dev ** 2)
    pdf = coefficient * math.exp(exponent)
    return pdf

# Example usage
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution
x = 1.5  # Point at which to calculate the PDF

pdf_value = normal_pdf(x, mean, std_dev)
print("PDF at x =", x, "is", pdf_value)


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
n = 1000  # Sample size
p = 0.4  # Probability of success

# Generate the random sample
sample = np.random.binomial(n=1, p=p, size=n)
print(sample)
print(len(sample))
# Plot the histogram
plt.hist(sample, bins=2, edgecolor='black')
plt.xlabel('Success (1) / Failure (0)')
plt.ylabel('Frequency')
plt.title('Binomial Distribution - Random Sample')
plt.show()


# #5
# fixed number of trials: The binomial distribution is characterized by a fixed number of independent trials denoted by 'n'. Each trial can result in one of two outcomes, typically referred to as success or failure.
# 
# Independent and identical trials: The trials in a binomial distribution are assumed to be independent, meaning the outcome of one trial does not affect the outcome of another. Additionally, the probability of success ('p') remains constant across all trials.
# 
# Dichotomous outcomes: The outcomes of each trial in a binomial distribution are mutually exclusive and dichotomous, meaning they can be categorized as either success or failure.
# 
# Constant probability of success: The probability of success ('p') remains the same for each trial. The probability of failure ('q') is equal to 1 - p.
# 
# Counting successes: The binomial distribution focuses on counting the number of successes ('k') that occur in 'n' independent trials.
# 
# Examples of events where the binomial distribution can be applied are:
# 
# Coin Flipping: Consider a fair coin being flipped 10 times, and we want to know the probability of obtaining a certain number of heads (successes). Here, each flip can be considered as a trial, and the outcome of each flip can be categorized as either a head or a tail.
# 
# Drug Testing: In a clinical trial, a new drug is administered to a group of patients, and we want to determine the probability of a certain number of patients experiencing a positive response (success). Each patient can be considered as a trial, and the response can be categorized as either a success (positive response) or a failure (negative response

# In[5]:


#6

import math

def poisson_cdf(mean, k):
    cdf = 0
    for i in range(k + 1):
        cdf += math.exp(-mean) * (mean ** i) / math.factorial(i)
    return cdf


# In[6]:


mean = 3.5
point = 2
cdf = poisson_cdf(mean, point)
print(f"The cumulative probability at {point} for a Poisson distribution with mean {mean} is: {cdf}")


# #7
# The Binomial and Poisson distributions are both probability distributions used to model the number of events or successes, but they differ in certain characteristics and the situations in which they are applicable.
# 
# 1. Definition:
#    - Binomial Distribution: The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials. It has two parameters: n (number of trials) and p (probability of success in each trial).
#    - Poisson Distribution: The Poisson distribution models the number of events that occur in a fixed interval of time or space, assuming a constant average rate of occurrence (λ).
# 
# 2. Number of Trials or Observations:
#    - Binomial Distribution: The binomial distribution requires a fixed number of independent trials or observations (n) to be specified in advance.
#    - Poisson Distribution: The Poisson distribution does not require a fixed number of trials or observations. It models the number of events occurring in a fixed interval, and the interval can be of any length.
# 
# 3. Probability of Success or Rate of Occurrence:
#    - Binomial Distribution: The binomial distribution requires the probability of success (p) to be constant for each trial.
#    - Poisson Distribution: The Poisson distribution assumes a constant average rate of occurrence (λ) of events in the given interval.
# 
# 4. Shape and Limitations:
#    - Binomial Distribution: The binomial distribution is discrete and symmetric when p = 0.5. It is applicable when the number of trials is fixed, and each trial has only two possible outcomes (success or failure).
#    - Poisson Distribution: The Poisson distribution is also discrete but can approximate a continuous distribution. It is applicable when the number of events is rare, and the average rate of occurrence is moderate to large.
# 
# In summary, the binomial distribution is used when there is a fixed number of trials with a constant probability of success, while the Poisson distribution is used when the number of events is rare and the average rate of occurrence is known. The choice between the two distributions depends on the specific characteristics of the data and the nature of the problem being analyzed.

# #8
# import numpy as np
# mean=5
# sample= np.random.poisson(mean,size=1000)

# In[21]:


sample_mean=np.mean(sample)
sample_var=np.var(mean)


# In[22]:


print(sample_mean)
print(sample_var)


# #9
# Binomial Distribution:
# In the Binomial distribution, the mean and variance are directly related. If we denote the number of trials as n and the probability of success as p, then the mean (μ) of the Binomial distribution is given by μ = np, and the variance (σ^2) is given by σ^2 = np(1 - p).
# 
# The variance is determined by the product of the number of trials (n), the probability of success (p), and the complement of the probability of success (1 - p). As the probability of success changes, the spread or variability of the distribution changes accordingly. When p = 0.5, the distribution is most spread out (maximum variance), and it becomes less spread out as p deviates from 0.5 towards either extreme (0 or 1).
# 
# Poisson Distribution:
# In the Poisson distribution, the mean and variance are equal. The mean (μ) and variance (σ^2) of the Poisson distribution are both given by μ = σ^2 = λ, where λ is the average rate of occurrence or the expected number of events in the given interval.

# #10
# 
# 
# In a normal distribution, the least frequent data points are located in the tails of the distribution, farthest away from the mean.
# 
# In a symmetrical normal distribution, the mean is located at the center of the distribution, and the data is symmetrically distributed around it. The tails of the distribution represent the extreme values, both in the positive and negative directions.
# 
# Since the normal distribution is bell-shaped, the density of data points gradually decreases as you move away from the mean towards the tails. The data points in the tails are less frequent because they represent extreme values that are further away from the central tendency of the distribution.
