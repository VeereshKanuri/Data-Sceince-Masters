#!/usr/bin/env python
# coding: utf-8

# #1
# 
# three measures of central tendancy are mean, median, mode

# #2
# 
# mean: mean is also known as average , is found by summing up all the values in a dataset and dividing the total by number of values. he formula for the mean is:
# 
# Mean = (sum of all values) / (number of values)
# 
# The mean is sensitive to extreme values or outliers since it takes into account every value in the dataset.
# 
# median: median is the middle value of dataset when arranged in ascending or descending order.f the dataset has an odd number of values, the median is the middle value itself. If the dataset has an even number of values, the median is the average of the two middle values. The median is not influenced by extreme values or outliers and provides a measure of the central value. To find the median, the dataset must first be sorted.
# 
# mode: mode the value that is most repeated in dataset. Unlike the mean and median, which are calculated mathematically, the mode is determined by observation. A dataset can have multiple modes (multimodal) or no mode at all (no value appears more than once). The mode can be useful for identifying the most common or dominant value in a dataset.

# In[4]:


#3 Measure the three measures of central tendency for the given height data

list1=[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

import pandas as pd
import numpy as np
df=pd.DataFrame(list1)
mean= df[0].mean()
print(mean)
mode= df[0].mode()
print(mode)
median=df[0].median()
print(median)

np.mean(list1)
np.median(list1)


# In[5]:


#4

np.std(list1)


# #5
# 
# Range: The range is the simplest measure of dispersion and is calculated as the difference between the maximum and minimum values in a dataset. It provides an idea of the spread between the extreme values in the dataset. However, it does not consider the distribution of values within that range. For example, if you have a dataset of test scores ranging from 60 to 95, the range would be 35 (95 - 60), indicating the spread of scores.
# 
# Variance: Variance measures the average squared deviation of each data point from the mean of the dataset. It takes into account all values in the dataset and provides a measure of the overall spread. To calculate the variance, you subtract the mean from each data point, square the result, sum up the squared differences, and divide by the number of data points. For example, if you have a dataset of test scores [75, 80, 85, 90, 95], and the mean is 85, the variance would be calculated as (75-85)^2 + (80-85)^2 + (85-85)^2 + (90-85)^2 + (95-85)^2, divided by the number of data points.
# 
# Standard Deviation: The standard deviation is the square root of the variance. It measures the dispersion of data around the mean. It is widely used because it is in the same unit as the original dataset, making it more interpretable. It quantifies the average amount by which each data point deviates from the mean. For example, using the same test scores dataset as before, if the variance is calculated to be 25, the standard deviation would be the square root of 25, which is 5

# #6
# 
# 
# A Venn diagram is a graphical representation that uses overlapping circles or other shapes to depict the relationships between different sets or groups of items.In a Venn diagram, each circle or shape represents a set, and the overlapping regions show the common elements between the sets. The areas outside the circles represent elements that do not belong to any of the sets being compared.
# 
# Venn diagrams are commonly used to illustrate concepts related to set theory, logic, and categorical relationships. They provide a visual way to analyze and understand the relationships between different groups or categories of items.

# #7
# 
# 
# #For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
# (i) A B
# (ii) A ⋃ B

# In[7]:


A = {2,3,4,5,6,7} 
B = {0,2,6,8,10}
A.intersection(B)


# In[8]:


A.union(B)


# #8
# 
# Skewness in data refers to the measure of asymmetry or departure from symmetry in the distribution of values. It indicates whether the data is concentrated more towards one tail of the distribution or the other. Skewness is an important statistical concept that helps understand the shape and characteristics of a dataset.
# 
# There are three main types of skewness:
# 
# Positive Skewness (Right Skewness): In a positively skewed distribution, the tail on the right side of the distribution is longer or more spread out than the left side. This means that the majority of the data points are concentrated towards the left, and there are few extreme values on the right side.
# 
# here   mean > median > mode
# 
# Negative Skewness (Left Skewness): In a negatively skewed distribution, the tail on the left side of the distribution is longer or more spread out than the right side. The majority of the data points are concentrated towards the right, and there are few extreme values on the left side.
# 
# here   mode>median>mean
# 
# Zero Skewness: A dataset is considered to have zero skewness when it is perfectly symmetrical, meaning the distribution is evenly balanced around the mean, and both tails are of equal length.
# 
# here    mode=median=mean

# #9
# 
# 
# In a right-skewed distribution, the tail of the distribution is longer or more spread out on the right side, indicating the presence of a few extreme values in that direction. In this case, the mean will be larger than the median.
# 
# To understand this relationship, it's helpful to visualize the distribution. Imagine a right-skewed distribution with a long tail stretching towards the right. The mean is influenced by the extreme values on the right side, pulling it in that direction. As a result, the mean is typically larger than the median.
# 
# The median, on the other hand, represents the middle value when the data is arranged in ascending or descending order. Since the right-skewed distribution has a longer tail on the right, the extreme values on that side can pull the median towards the right, but to a lesser extent compared to the mean. Consequently, the median will generally be smaller than the mean in a right-skewed distribution.

# #10
# 
# Covariance and correlation are both measures used in statistical analysis to quantify the relationship between variables. While they are related, there are key differences between the two:
# 
# Covariance:
# Covariance measures the extent to which two variables vary together. It determines the direction (positive or negative) and strength of the linear relationship between two variables. A positive covariance indicates that the variables tend to move in the same direction, while a negative covariance indicates they move in opposite directions. However, covariance alone does not provide a standardized measure of the strength of the relationship or its reliability.
# 
# Covariance can be calculated using the following formula:
# 
# Cov(X, Y) = Σ((X - μX)(Y - μY)) / N
# 
# Where X and Y are the variables, μX and μY are their respective means, and N is the number of data points.
# 
# Correlation:
# Correlation is a standardized measure that quantifies the strength and direction of the linear relationship between two variables. It normalizes the covariance by dividing it by the product of the standard deviations of the variables. Correlation always ranges between -1 and 1, with -1 indicating a perfect negative linear relationship, 1 indicating a perfect positive linear relationship, and 0 indicating no linear relationship.
# 
# Correlation can be calculated using the following formula:
# 
# Corr(X, Y) = Cov(X, Y) / (σX * σY)
# 
# Where X and Y are the variables, Cov(X, Y) is the covariance, and σX and σY are the standard deviations of X and Y, respectively.
# 
# In statistical analysis, covariance and correlation are used to understand the relationship between variables and to make inferences about their behavior. Covariance is a raw measure that indicates the direction of the relationship, while correlation provides a standardized measure that allows for comparison between different pairs of variables. Correlation is particularly useful when comparing variables with different scales or units, as it standardizes the measure of association. It helps identify whether variables are positively or negatively related and the strength of that relationship.
# 
# Overall, correlation is a more widely used and interpretable measure than covariance, as it provides standardized values and is not affected by the scale or unit of measurement of the variables.

# #11
# 
# The formula for calculating the sample mean, denoted as "x̄" (pronounced "x-bar"), is the sum of all the values in the dataset divided by the total number of values.
# 
# Mathematically, the formula for the sample mean is:
# 
# x̄ = (x₁ + x₂ + x₃ + ... + xₙ) / n
# 
# Where:
# 
# x₁, x₂, x₃, ..., xₙ represents the individual values in the dataset.
# n represents the total number of values in the dataset.
# Here's an example calculation to find the sample mean of a dataset:
# 
# Consider the dataset: 7, 4, 9, 2, 6
# 
# To find the sample mean, we sum up all the values and divide by the total number of values:
# 
# x̄ = (7 + 4 + 9 + 2 + 6) / 5
# 
# x̄ = 28 / 5
# 
# x̄ = 5.6

# #12
# 
# For a normal distribution, the relationship between the measures of central tendency, namely the mean, median, and mode, is as follows:
# 
# Mean: In a normal distribution, the mean, median, and mode are all equal. The mean represents the arithmetic average of the data points and is located at the center of the distribution.
# 
# Median: The median is also located at the center of a normal distribution. Since a normal distribution is symmetric, the median is the same as the mean. It divides the data into two equal halves, with 50% of the data falling below the median and 50% above.
# 
# Mode: The mode of a normal distribution is also equal to the mean and median. In a perfectly symmetric normal distribution, there is a single mode, which corresponds to the peak or highest point of the distribution.
# 
# In summary, for a normal distribution, the mean, median, and mode are all equal and located at the center of the distribution. This reflects the symmetrical nature of the normal distribution, where the data is evenly balanced around the central point.

# #13
# 
# Covariance and correlation are both measures used to quantify the relationship between variables, but they have some key differences:
# 
# 1. Measurement Units:
# Covariance is measured in the units of the product of the two variables being analyzed. For example, if one variable is measured in kilograms and the other in meters, the covariance will be expressed in kilogram-meters. On the other hand, correlation is a dimensionless quantity, ranging from -1 to 1, without any specific units.
# 
# 2. Scale Independence:
# Covariance is influenced by the scales of the variables being analyzed. Variables with larger magnitudes will tend to have larger covariances. Correlation, however, is scale-independent. It standardizes the covariance by dividing it by the product of the standard deviations of the variables, resulting in a value between -1 and 1.
# 
# 3. Interpretation:
# Covariance measures the direction and magnitude of the linear relationship between variables. A positive covariance indicates a positive linear relationship, while a negative covariance indicates a negative linear relationship. However, the magnitude of the covariance does not provide a clear indication of the strength or reliability of the relationship. Correlation, on the other hand, not only provides information about the direction of the relationship but also quantifies the strength and reliability of the linear association. A correlation value close to 1 or -1 indicates a strong linear relationship, while a value close to 0 indicates a weak or no linear relationship.
# 
# 4. Range of Values:
# Covariance can take any value, positive, negative, or zero, depending on the nature of the relationship between variables. Correlation, however, is always bounded between -1 and 1. A correlation of 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.
# 
# In summary, covariance measures the direction and magnitude of the linear relationship between variables, while correlation provides a standardized measure of the strength and direction of the linear association. Covariance is influenced by the units and scales of the variables, while correlation is scale-independent and ranges between -1 and 1. Correlation is a more commonly used and interpretable measure as it allows for comparison between different pairs of variables.

# #14
# 
# Outliers can have a significant impact on measures of central tendency and dispersion, leading to distortions in the overall understanding of the data. Here's how outliers affect these measures:
# 
# 1. Measures of Central Tendency:
#    - Mean: Outliers, especially extreme values, can pull the mean towards their direction. This is because the mean is sensitive to extreme values and is influenced by their magnitudes. As a result, the mean may not accurately represent the typical or average value of the dataset.
#    - Median: The median is generally more robust to outliers compared to the mean. Outliers have minimal impact on the median since it only considers the middle value(s) and is not influenced by extreme values. Therefore, the median is often preferred when dealing with skewed distributions or datasets containing outliers.
#    - Mode: The mode is unaffected by outliers as it represents the most frequently occurring value(s) in the dataset. Outliers, being relatively rare occurrences, do not alter the mode significantly.
# 
# 2. Measures of Dispersion:
#    - Range: Outliers can significantly impact the range as they may fall far outside the normal range of values. The range is simply the difference between the maximum and minimum values in the dataset, so outliers can widen the range and distort the spread of the remaining data.
#    - Variance and Standard Deviation: Outliers can increase the variance and standard deviation. Since these measures quantify the average distance of each data point from the mean, outliers with large deviations from the mean contribute disproportionately to the overall dispersion. As a result, the variance and standard deviation can be inflated by the presence of outliers.
#    - Interquartile Range (IQR): The IQR is a robust measure of dispersion that is less affected by outliers. It considers the range between the upper quartile (75th percentile) and the lower quartile (25th percentile), which makes it less sensitive to extreme values. Consequently, the IQR provides a more reliable measure of the spread in the presence of outliers.
# 
# Example: Consider a dataset of exam scores: 70, 75, 80, 85, 90, 95, and an outlier of 50. The presence of the outlier can significantly affect the measures of central tendency and dispersion:
# 
# - Mean: Without the outlier, the mean would be (70 + 75 + 80 + 85 + 90 + 95) / 6 = 83.33. However, with the outlier included, the mean becomes (70 + 75 + 80 + 85 + 90 + 95 + 50) / 7 = 78.57, pulling the mean towards the lower end.
# - Median: The median remains the same (80) regardless of the outlier since it only considers the middle value.
# - Range: The range is significantly affected by the outlier. Without the outlier, the range is 95 - 70 = 25, but with the outlier included, the range becomes 95 - 50 = 45, indicating a wider spread.
# - Variance and Standard Deviation: The outlier's large deviation from the mean can inflate the variance and standard deviation, indicating higher dispersion.
# - Interquartile Range (IQR): The IQR is less affected by the outlier since it considers the middle 50% of the data, making it a more robust measure of dispersion.
# 
# In summary, outliers can distort measures of central tendency (such as mean) and dispersion (such as range, variance, and standard deviation). It is important to be cautious when interpreting these measures in the presence of outliers, and it may be necessary to explore additional robust measures that are less sensitive to extreme values.
