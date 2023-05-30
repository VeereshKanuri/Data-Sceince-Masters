#!/usr/bin/env python
# coding: utf-8

# #1
# 
# scatterplot(): scatter plot is used to visualise the relationship between two continuous varaibles. it displays invidual data points as a marker on two dimensional plane. Scatter plots help identify patterns, trends, clusters, or outliers in the data. Seaborn's scatterplot() function is commonly used to create scatter plots.
# 
# sns.scatterplot()
# 
# histogram(): histograms are used to visualise the distribution of a single variable. they divide data into equal bins and display the frequency or count of data points falling within each bin. Histograms help understand the shape, central tendency, and dispersion of the data. Seaborn's histplot() function can be used to create histograms.
# 
# sns.histplot()
# 
# Bar Plot:
# Bar plots, or bar charts, are used to compare categorical variables. They display the frequency, count, or average value of different categories as rectangular bars. Bar plots are useful for comparing data across categories and identifying trends or differences. Seaborn's barplot() function is commonly used for creating bar plots.
# sns.barplot()
# 
# Box Plot:
# Box plots, also known as box-and-whisker plots, provide a summary of the distribution of a continuous variable across different categories. They display the median, quartiles, and potential outliers in the data. Box plots are useful for visualizing the central tendency, dispersion, and skewness of data. Seaborn's boxplot() function is commonly used to create box plots.
# 
# sns.boxplot()
# 
# Heatmap:
# Heatmaps are used to visualize the correlation or relationship between variables in a matrix format. They use a color gradient to represent the strength or magnitude of the relationship between variables. Heatmaps help identify patterns, clusters, or dependencies between variables. Seaborn's heatmap() function is commonly used to create heatmaps
# 
# sns.heatmap()

# In[3]:


#2
import seaborn as sns
ds=sns.load_dataset('fmri')


# In[4]:


ds


# In[10]:


sns.lineplot(x=ds.timepoint,y =ds.signal,hue=ds.event,style=ds.region)


# In[11]:


#3
ds3=sns.load_dataset('titanic')


# In[18]:


ds3


# In[19]:


import matplotlib.pyplot as plt

plt.subplot(1,2,1)
sns.boxplot(x='pclass',y='age',data=ds3)
plt.subplot(1,2,2)
sns.boxplot(x='pclass',y='fare',data=ds3)
plt.tight_layout()


# In[21]:


#4
ds4=sns.load_dataset('diamonds')


# In[22]:


ds4


# In[23]:


sns.histplot(ds4['price'])


# In[29]:


sns.histplot(x='price',data=ds4,hue='cut',kde=True)


# In[30]:


#5
ds5=sns.load_dataset('iris')


# In[31]:


ds5


# In[35]:


sns.pairplot(ds5,hue='species')


# In[36]:


#6
ds6=sns.load_dataset('flights')


# In[37]:


ds6


# In[47]:


flights_matrix = ds6.pivot("month", "year", "passengers")

# Create the heatmap
sns.heatmap(flights_matrix, cmap="YlGnBu")


# In[ ]:




