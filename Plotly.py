#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import seaborn as sns
ds=sns.load_dataset('titanic')


# In[2]:


ds


# In[5]:


import plotly.graph_objects as go


# In[7]:


fig=go.Figure()


# In[15]:


fig.add_traces(go.Scatter(x=ds.age,y=ds.fare,marker=dict(size=8, line=dict(width=0))))


# In[13]:


ds2=sns.load_dataset("tips")


# In[14]:


ds2


# In[16]:


import plotly.express as px


# In[18]:


px.box(ds2,x='day',y='total_bill',color='smoker')


# In[26]:


px.histogram(ds2, x='sex', y='total_bill', color='day', pattern_shape='smoker')


# In[27]:


import plotly.express as px


# In[28]:


ds3=sns.load_dataset('iris')


# In[29]:


px.scatter_matrix(ds3, dimensions=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], color='species')


# # 5
# Distplot is a visualization technique used to display the distribution of a univariate (single variable) dataset. It combines a histogram with a kernel density estimate plot to provide a comprehensive view of the data distribution. The histogram shows the frequency of values within different bins, while the kernel density estimate plot represents the smooth estimate of the probability density function.

# In[ ]:




