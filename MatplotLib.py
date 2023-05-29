#!/usr/bin/env python
# coding: utf-8

# #1
# 
# Matplotlib is a powerful data visualization library in Python. It provides a wide range of tools for creating high-quality plots, charts, and graphs. The main purpose of Matplotlib is to help users visualize their data in a meaningful and informative way.
# 
# Here are some key reasons why Matplotlib is commonly used:
# 
# Data Visualization: Matplotlib allows users to create various types of plots, enabling them to explore and understand their data. It provides an extensive set of plotting functions and options to customize the visual representation of data.
# 
# Flexibility: Matplotlib is highly flexible and can handle a wide range of plotting requirements. It supports a variety of plot types, works well with different data structures, and provides a high level of control over plot aesthetics.
# 
# Integration: Matplotlib integrates well with other scientific computing libraries in Python such as NumPy and pandas. It can directly plot data from these libraries' data structures, making it easy to incorporate data visualization into data analysis workflows.
# 
# Publication-Quality Output: Matplotlib is capable of generating high-quality plots suitable for publication and presentations. It provides fine-grained control over plot elements, allowing users to customize colors, fonts, annotations, and other visual aspects to create professional-looking visualizations.
# 
# Five plots that can be created using the Pyplot module of Matplotlib are:
# 
# Line Plot: A basic plot that represents data points connected by straight lines. It is commonly used to show trends and patterns in data over a continuous variable.
# 
# Scatter Plot: A plot that displays individual data points as markers in a two-dimensional space. It is useful for visualizing the relationship between two variables and identifying patterns or clusters.
# 
# Bar Chart: A chart that represents categorical data using rectangular bars. It is commonly used to compare different categories or groups.
# 
# Histogram: A graphical representation of the distribution of numerical data. It divides the data into bins and shows the frequency or count of data points falling into each bin.
# 
# Pie Chart: A circular chart divided into slices to represent the proportion of different categories or parts of a whole. It is useful for displaying relative proportions or percentages6

# #1
# Scatter Plot: A plot that displays individual data points as markers in a two-dimensional space. It is useful for visualizing the relationship between two variables and identifying patterns or clusters.

# In[6]:



import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))


# In[7]:


x


# In[8]:


y


# In[11]:


plt.scatter(x,y)
plt.xlabel("this is my x axis")
plt.ylabel("this is my y label")
plt.title("assignment plot")


# #3
# 
# The subplot() function in Matplotlib is used to create a grid of subplots within a single figure. It allows you to display multiple plots or visualizations in a single figure window, organized in rows and columns.
# 
# subplot(nrows, ncols, plot_number)
# nrows represents the number of rows in the subplot grid.
# ncols represents the number of columns in the subplot grid.
# plot_number specifies the current plot's position in the grid.
# 
# 
# 
# 
# 

# In[14]:


import numpy as np
import matplotlib.pyplot as plt

# Data for line plots
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])


# In[17]:


plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.title("line 1")

plt.subplot(2,2,2)
plt.plot(x2,y2)
plt.title("line 2")

plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.title("line 3")

plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.title("line 4")

plt.tight_layout() # Adjust the spacing between subplots

plt.show()


# #4
# 
# 
# A bar plot, also known as a bar chart or bar graph, is a visualization that uses rectangular bars to represent categorical data. It displays the relationship between a categorical variable and a corresponding numerical value or frequency.
# 
# Bar plots are used to:
# 
# Compare Data: Bar plots are effective for comparing the magnitudes or values of different categories. They allow you to quickly identify and visualize the differences or similarities between different groups or categories.
# 
# Display Frequency or Count: Bar plots can represent the frequency or count of data points within each category. This is useful when you want to visualize the distribution or occurrence of different categories.
# 
# Present Rankings or Order: Bar plots can be used to display rankings or order of categories based on their values. The lengths or heights of the bars represent the relative values, allowing for easy interpretation of the order.
# 
# Show Patterns or Trends: Bar plots can reveal patterns or trends in data across categories. By plotting the data in a bar chart, you can identify increases, decreases, or other patterns within different categories.
# 
# Visualize Categorical Data: Bar plots are particularly useful for visualizing categorical data where the categories are distinct and non-overlapping. Each category is represented by a separate bar, making it visually clear and intuitive.

# In[21]:


company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.subplot(1,2,1)
plt.bar(company,profit)
plt.subplot(1,2,2)
plt.barh(company,profit)
plt.tight_layout()


# In[30]:


#5

import numpy as np
import matplotlib.pyplot as plt

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
plt.boxplot([box1,box2])


# In[ ]:




