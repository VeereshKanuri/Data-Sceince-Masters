#!/usr/bin/env python
# coding: utf-8

# #1
# 
# A t-test is used when the population standard deviation is unknown or when the sample size is small (typically n < 30)
# On the other hand, a z-test is used when the population standard deviation is known or when the sample size is large (typically n ≥ 30). In a z-test, the population standard deviation is known, and the standard normal (z) distribution is used to calculate the test statistic

# #2
# 
# 
# One-Tailed Test:
# A one-tailed test, also known as a directional test, is a hypothesis test where the alternative hypothesis is stated in a specific direction. It tests for the possibility of a relationship or difference in only one direction. The critical region is located entirely in one tail of the distribution. The decision to reject or fail to reject the null hypothesis is based on the observation falling in that specific tail.
# 
# A two-tailed test, also known as a non-directional test, is a hypothesis test where the alternative hypothesis is stated without a specific direction. It tests for the possibility of a relationship or difference in both directions. The critical region is divided between the two tails of the distribution. The decision to reject or fail to reject the null hypothesis is based on the observation falling in either tail.

# #3
# 
# Type I Error: A Type I error, also known as a "false positive," occurs when the null hypothesis is rejected when it is actually true. In other words, it is the incorrect rejection of a true null hypothesis. 
# 
# Type II Error: A Type II error, also known as a "false negative," occurs when the null hypothesis is failed to be rejected when it is actually false. In other words, it is the failure to reject a false null hypothesis

# #4
# 
# how to update the probability of an event based on new evidence or information. It provides a way to calculate the conditional probability of an event given prior knowledge or information about related events.
# 
# The theorem can be stated as follows:
# 
# P(A|B) = (P(B|A) * P(A)) / P(B)
# 
# where:
# 
# P(A|B) represents the probability of event A occurring given that event B has occurred.
# P(B|A) represents the probability of event B occurring given that event A has occurred.
# P(A) represents the prior probability of event A occurring.
# P(B) represents the prior probability of event B occurring.

# #5
# 
# A confidence interval is a range of values that is used to estimate an unknown population parameter, such as the mean or proportion, based on a sample from that population. It provides a measure of the uncertainty associated with the estimation.
# 
# To calculate a confidence interval, you typically need three pieces of information:
# 1. The sample statistic (e.g., mean or proportion) that estimates the population parameter.
# 2. The standard error, which quantifies the variability or uncertainty of the sample statistic.
# 3. The desired level of confidence, which determines the width of the interval.
# 
# Here's an example to illustrate the calculation of a confidence interval:
# 
# Let's say you want to estimate the average height of all adult males in a certain city. You collect a random sample of 100 adult males and measure their heights. The sample mean height is found to be 175 cm, and the sample standard deviation is 5 cm.
# 
# Now, let's calculate a 95% confidence interval for the population mean height.
# 
# First, determine the standard error. Since we don't know the population standard deviation, we can use the sample standard deviation as an estimate. The standard error (SE) is calculated as:
# 
# SE = sample standard deviation / sqrt(sample size)
# SE = 5 cm / sqrt(100)
# SE = 0.5 cm
# 
# Next, determine the critical value corresponding to the desired level of confidence. For a 95% confidence level, the critical value can be obtained from a standard normal distribution. In this case, the critical value is approximately 1.96 (you can use a z-table or a calculator to find this value).
# 
# Finally, calculate the confidence interval using the formula:
# 
# Confidence interval = sample mean ± (critical value * standard error)
# 
# Confidence interval = 175 cm ± (1.96 * 0.5 cm)
# 
# The confidence interval for the average height of all adult males in the city is approximately 174.04 cm to 175.96 cm.
# 
# This means that we are 95% confident that the true population mean height falls within this interval. It provides a range of plausible values based on the sample data and accounts for the uncertainty associated with estimation.

# #6
# 
# Certainly! Here's an example problem that demonstrates the application of Bayes' Theorem:
# 
# Problem:
# A certain disease affects 1% of the population. There is a diagnostic test for this disease that has an accuracy rate of 95%. If a person tests positive for the disease, what is the probability that they actually have the disease?
# 
# Solution:
# To solve this problem using Bayes' Theorem, we need to consider the following probabilities:
# - P(D) = Probability of having the disease = 0.01 (prior probability)
# - P(~D) = Probability of not having the disease = 0.99 (complement of P(D))
# - P(Pos|D) = Probability of testing positive given that the person has the disease = 0.95 (accuracy rate)
# - P(Pos|~D) = Probability of testing positive given that the person does not have the disease = 0.05 (false positive rate)
# 
# We want to calculate P(D|Pos), which is the probability of having the disease given that the person tested positive.
# 
# According to Bayes' Theorem:
# P(D|Pos) = (P(Pos|D) * P(D)) / P(Pos)
# 
# To calculate P(Pos), we need to consider both true positive and false positive scenarios:
# P(Pos) = P(Pos|D) * P(D) + P(Pos|~D) * P(~D)
# 
# Now, let's substitute the values into the formula:
# 
# P(Pos) = (0.95 * 0.01) + (0.05 * 0.99)
#        = 0.0095 + 0.0495
#        = 0.059
# 
# P(D|Pos) = (0.95 * 0.01) / 0.059
#          ≈ 0.161
# 
# Therefore, the probability of a person actually having the disease given that they tested positive is approximately 0.161, or 16.1%.
# 
# This calculation shows that even with a relatively accurate test (95% accuracy), the probability of having the disease is still relatively low (16.1%) when the disease prevalence in the population is low (1%).

# #7
# 
# Confidence Interval = Sample Mean ± (Critical Value * Standard Error)
# 
# 
# Determine the critical value. For a 95% confidence interval, the critical value is based on the standard normal distribution (Z-distribution) and is approximately 1.96.
# 
# Calculate the standard error. The standard error represents the standard deviation of the sampling distribution and is calculated by dividing the sample standard deviation by the square root of the sample size. In this case, the standard error is 5 / √n, where n is the sample size.
# 
# Substitute the values into the formula:
# Confidence Interval = 50 ± (1.96 * (5 / √n))
# 
# As the sample size increases, the confidence interval will become narrower, indicating a more precise estimate of the population mean. The interpretation of the confidence interval is that we are 95% confident that the true population mean falls within the calculated range.

# #8
# 
# The margin of error in a confidence interval represents the range of values around the point estimate (such as the sample mean) that is likely to contain the true population parameter with a certain level of confidence. It quantifies the uncertainty in our estimate.
# 
# The margin of error is influenced by several factors, including the sample size, variability of the data, and the desired level of confidence. In general, as the sample size increases, the margin of error decreases.
# 
# A larger sample size reduces the margin of error because it provides more information and reduces the variability in the data. With a larger sample size, the estimate of the population parameter becomes more precise, resulting in a narrower confidence interval.
# 
# For example, consider two scenarios:
# 
# Scenario 1: A survey is conducted with a sample size of 100 respondents. The margin of error for a 95% confidence interval is ±3%.
# 
# Scenario 2: Another survey is conducted with a larger sample size of 1000 respondents. The margin of error for a 95% confidence interval is ±1%.
# 
# In Scenario 2, the larger sample size leads to a smaller margin of error compared to Scenario 1. This means that the estimate obtained from the larger sample is more precise and provides a narrower range of values that is likely to contain the true population parameter.
# 
# In summary, a larger sample size reduces the margin of error, providing a more accurate and precise estimate of the population parameter.

# #9
# 
# To calculate the z-score, we can use the formula:
# 
# z = (x - μ) / σ
# 
# where:
# - x is the value of the data point
# - μ is the population mean
# - σ is the population standard deviation
# 
# Let's calculate the z-score using the given values:
# 
# x = 75
# μ = 70
# σ = 5
# 
# z = (75 - 70) / 5
# z = 1
# 
# The calculated z-score is 1.
# 
# Interpretation: The z-score represents the number of standard deviations that the data point is away from the population mean. In this case, a z-score of 1 indicates that the data point is 1 standard deviation above the population mean. This means that the data point, with a value of 75, is higher than the average value (70) by one standard deviation (which is 5 in this case).

# #10
# 
# Null Hypothesis (H0): The new weight loss drug is not significantly effective.
# Alternative Hypothesis (Ha): The new weight loss drug is significantly effective.
# 
# Since we are comparing the sample mean (6 pounds) to a hypothesized population mean, we can use a one-sample t-test. Here are the steps to perform the t-test:
# 
# 1. Set the significance level (alpha). In this case, the confidence level is 95%, which corresponds to an alpha of 0.05.
# 
# 2. Calculate the t-statistic using the formula:
#    t = (sample_mean - hypothesized_mean) / (sample_standard_deviation / sqrt(sample_size))
# 
#    Given:
#    Sample mean (x̄) = 6 pounds
#    Hypothesized mean (μ) = 0 (since the null hypothesis assumes no effect)
#    Sample standard deviation (s) = 2.5 pounds
#    Sample size (n) = 50 participants
# 
#    t = (6 - 0) / (2.5 / sqrt(50))
#    Calculate the value of t.
# 
# 3. Determine the critical value. Since this is a one-sample t-test with a 95% confidence level and 50 participants (df = 50-1 = 49), the critical value can be obtained from the t-distribution table or a statistical software.
# 
# 4. Compare the calculated t-statistic with the critical value:
#    - If the calculated t-statistic is greater than the critical value, reject the null hypothesis.
#    - If the calculated t-statistic is less than or equal to the critical value, fail to reject the null hypothesis.
# 
# 5. Calculate the p-value associated with the t-statistic. The p-value represents the probability of observing a t-statistic as extreme as the calculated value, assuming the null hypothesis is true. The p-value can be obtained from the t-distribution table or by using statistical software.
# 
# 6. Compare the p-value with the significance level (alpha):
#    - If the p-value is less than the significance level, reject the null hypothesis.
#    - If the p-value is greater than or equal to the significance level, fail to reject the null hypothesis.
# 
# By following these steps, you can determine whether the weight loss drug is significantly effective based on the given sample data and the chosen significance level.
# 

# #11
# 
# To calculate the 95% confidence interval for the true proportion of people satisfied with their job, we can use the following formula:
# 
# Confidence Interval = sample proportion ± margin of error
# 
# Given information:
# - Sample size (n) = 500
# - Proportion of people satisfied (p) = 65% or 0.65
# 
# Now, let's calculate the confidence interval:
# 
# 1. Calculate the standard error:
#    Standard Error (SE) = sqrt((p * (1 - p)) / n)
# 
#    SE = sqrt((0.65 * (1 - 0.65)) / 500)
#    Calculate the value of SE.
# 
# 2. Determine the z-value for the desired confidence level. For a 95% confidence level, the corresponding z-value can be obtained from the standard normal distribution table or using statistical software. The z-value for a 95% confidence level is approximately 1.96.
# 
# 3. Calculate the margin of error:
#    Margin of Error = z-value * SE
# 
#    Margin of Error = 1.96 * SE
#    Calculate the value of the margin of error.
# 
# 4. Calculate the lower and upper bounds of the confidence interval:
#    Lower Bound = sample proportion - margin of error
#    Upper Bound = sample proportion + margin of error
# 
#    Lower Bound = 0.65 - margin of error
#    Upper Bound = 0.65 + margin of error
#    Calculate the values of the lower and upper bounds.
# 
# The resulting confidence interval represents the range within which we can be 95% confident that the true proportion of people satisfied with their job lies.
# 
# For example, let's assume the calculated margin of error is 0.03. Then, the 95% confidence interval would be:
# 
# Lower Bound = 0.65 - 0.03 = 0.62
# Upper Bound = 0.65 + 0.03 = 0.68
# 
# Interpretation: We can be 95% confident that the true proportion of people satisfied with their job lies between 0.62 and 0.68.

# #12
# 
# To conduct a hypothesis test to determine if there is a significant difference in student performance between two teaching methods, we can use a t-test. Here's how to proceed:
# 
# Null Hypothesis (H0): The mean scores of sample A and sample B are equal.
# Alternative Hypothesis (Ha): The mean scores of sample A and sample B are significantly different.
# 
# Given information:
# Sample A: mean = 85, standard deviation = 6
# Sample B: mean = 82, standard deviation = 5
# Significance level (α) = 0.01
# 
# Let's perform the hypothesis test:
# 
# 1. Calculate the t-score:
#    The formula for the t-score is:
#    t = (mean_A - mean_B) / sqrt((s1^2 / n1) + (s2^2 / n2))
#    where mean_A and mean_B are the means of sample A and sample B, s1 and s2 are their respective standard deviations, and n1 and n2 are the sample sizes.
# 
#    t = (85 - 82) / sqrt((6^2 / n1) + (5^2 / n2))
# 
# 2. Determine the degrees of freedom (df):
#    df = n1 + n2 - 2
#    where n1 and n2 are the sample sizes of sample A and sample B, respectively.
# 
# 3. Determine the critical t-value:
#    Since the significance level is 0.01 and we are performing a two-tailed test, we need to find the critical t-value that corresponds to a significance level of 0.005 (0.01 divided by 2) and the degrees of freedom obtained in step 2. You can refer to a t-distribution table or use statistical software to find the critical t-value.
# 
# 4. Compare the calculated t-score with the critical t-value:
#    If the calculated t-score is greater than the critical t-value, we reject the null hypothesis. Otherwise, we fail to reject the null hypothesis.
# 
# If we reject the null hypothesis, it indicates that there is a significant difference in student performance between the two teaching methods.
# 
# Note: Since the sample sizes and population parameters are not provided, we cannot calculate the exact t-score and critical t-value in this case. However, you can follow the steps outlined above using the given information to perform the hypothesis test.

# #13
# 
# To calculate the 90% confidence interval for the true population mean, we can use the formula:
# 
# Confidence Interval = sample mean ± (critical value * standard error)
# 
# Given information:
# Population mean (μ) = 60
# Standard deviation (σ) = 8
# Sample mean (x̄) = 65
# Sample size (n) = 50
# Confidence level = 90%
# 
# First, we need to calculate the critical value corresponding to the 90% confidence level. Since the sample size is large (n > 30) and the population standard deviation is known, we can use the z-score.
# 
# 1. Find the z-score for a 90% confidence level:
#    For a 90% confidence level, the area under the normal distribution curve is divided equally into two tails, resulting in an alpha value of (1 - 0.90) / 2 = 0.05.
#    Using a standard normal distribution table or a statistical software, we find the z-score corresponding to an alpha value of 0.05, which is approximately 1.645.
# 
# 2. Calculate the standard error:
#    The standard error (SE) represents the standard deviation of the sample mean and is calculated as:
#    SE = σ / √n
#    where σ is the population standard deviation and n is the sample size.
# 
#    SE = 8 / √50
# 
# 3. Calculate the confidence interval:
#    Confidence Interval = x̄ ± (z * SE)
#    where x̄ is the sample mean, z is the critical value, and SE is the standard error.
# 
#    Confidence Interval = 65 ± (1.645 * (8 / √50))
# 
# Calculating the numerical values will give you the specific confidence interval for the true population mean.
# 
# Interpretation:
# The 90% confidence interval calculated represents a range of values within which we are 90% confident that the true population mean lies. This means that if we were to repeat the sampling process multiple times, we would expect the true population mean to fall within this interval 90% of the time.

# #14
# 
# To conduct a hypothesis test to determine if caffeine has a significant effect on reaction time, we need to establish the null hypothesis (H0) and the alternative hypothesis (H1).
# 
# Null hypothesis (H0): Caffeine has no significant effect on reaction time. The mean reaction time for participants is not significantly different from the population mean.
# Alternative hypothesis (H1): Caffeine has a significant effect on reaction time. The mean reaction time for participants is significantly different from the population mean.
# 
# Given information:
# Sample size (n) = 30
# Sample mean (x̄) = 0.25 seconds
# Sample standard deviation (s) = 0.05 seconds
# Confidence level = 90% (which corresponds to a significance level of 0.10)
# 
# Now, we can perform a t-test to test the hypotheses. The steps involved are as follows:
# 
# 1. Set up the hypotheses:
#    H0: μ = μ0 (population mean reaction time is equal to a specified value, typically 0)
#    H1: μ ≠ μ0 (population mean reaction time is not equal to the specified value)
# 
# 2. Calculate the t-score:
#    t_score = (x̄ - μ0) / (s / √n)
# 
#    In this case, since the null hypothesis states that caffeine has no effect, we can set μ0 = 0.
# 
#    t_score = (0.25 - 0) / (0.05 / √30) = 15
# 
# 3. Determine the critical value:
#    Since we are conducting a two-tailed test and the significance level is 0.10 (corresponding to a 90% confidence level), we divide the significance level by 2 to get 0.05.
#    The critical value for a t-test with 29 degrees of freedom and a significance level of 0.05 is approximately ±1.699 (obtained from a t-distribution table or a calculator).
# 
# 4. Compare the t-score with the critical value:
#    If the t-score is greater than the positive critical value or less than the negative critical value, we reject the null hypothesis. Otherwise, we fail to reject the null hypothesis.
# 
#    In this case, the t-score of 15 is much larger than the critical value of ±1.699. Therefore, we reject the null hypothesis.
# 
# 5. State the conclusion:
#    Based on the results of the t-test, there is strong evidence to suggest that caffeine has a significant effect on reaction time.
# 
# In summary, at a 90% confidence level, the hypothesis test indicates that caffeine has a significant effect on reaction time.
