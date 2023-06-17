#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings 
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_excel("flight_price.xlsx")


# # 1

# In[3]:


df.ndim


# In[4]:


df.shape


# - 10683 rows and 11 columns 

# # 2

# In[5]:


df.columns


# In[6]:


df.isnull().sum()


# In[7]:


df.info()


# In[8]:


plt.hist(x=df['Price'],bins=20,edgecolor='black')
plt.xlabel("flight price")
plt.ylabel("Frequency")
plt.title("Distribution of Flight Prices")


# # 3

# In[9]:


df['Price'].describe()


# # 4

# In[10]:


df['Airline'].unique()


# In[11]:


df


# In[12]:


plt.figure(figsize=(25,10))
sns.boxplot(x=df['Airline'],y=df['Price'])
plt.xlabel('Airlines')
plt.ylabel("Prices")
plt.title("AIRLINES VS PRICES")
plt.tight_layout()
plt.show()


# - Skewed Statistical Measures: Outliers can significantly affect statistical measures such as the mean and standard deviation, making them less representative of the overall data.
# - Biased Results: If outliers are not properly handled, they can bias the results and lead to misleading conclusions.
# - Model Performance: Outliers may influence the performance of predictive models by disproportionately affecting the training process or model predictions.
# - Data Interpretation: Outliers can distort the interpretation of the relationship between variables or the distribution of the data.

# # 6

# In[13]:


df.info()


# In[14]:


df.head()


# In[15]:


df['Date_of_Journey']=pd.to_datetime(df['Date_of_Journey'])


# In[16]:


df['month']=df['Date_of_Journey'].dt.month


# In[17]:


df['month'].mode()


# In[18]:



# Resetting index to make 'month' a regular column
df = df.reset_index()

# Plotting the bar chart
df.groupby('month')['month'].count().plot.bar()

# Setting labels and title
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Flight Count by Month')

# Displaying the bar chart
plt.show()


# - we can observe in the month june most of the flight tickets will be booked 
# - we can also say that  march and may are also peak seasons

# # 76

# In[19]:


df['Duration']=pd.to_timedelta(df['Duration'])


# In[20]:


df['hour_dur']=df['Duration'].dt.components['hours']


# In[21]:


df['days_dur']=df['Duration'].dt.components['days']


# In[22]:


df['min_dur']=df['Duration'].dt.components['minutes']


# In[23]:


df['total_dur']=(df['hour_dur']*60)+(df['min_dur'])+(df['days_dur']*24*60)


# In[24]:


df


# In[25]:


sns.lineplot(x=df['total_dur'],y=df['Price'])


# In[26]:


plt.figure(figsize=(30,10))
sns.barplot(x=df['Airline'],y=df['Price'])
plt.show()


# In[27]:


df['Total_Stops']


# In[28]:


df['Total_Stops']=df['Total_Stops'].map({'non-stop':0,'2 stops':2,'1 stop':1,'3 stops':3,'4 stops':4})


# In[29]:


df


# In[30]:


df.groupby('Total_Stops')['Price'].mean().plot.bar()


# In[31]:


sns.barplot(x=df['Total_Stops'],y=df['Price'])


# # from above visulaizations we can observe that
# - with increase in no of stops price increases 
# - price is influenced by the duration of travel
# - price is influenced by the airlines 

# In[32]:


df.corr()


# #  8

# In[33]:


df3= pd.read_csv('googleplaystore.csv')


# In[34]:


df3


# In[35]:


df3.ndim


# In[36]:


df3.shape


# In[37]:


df3.info()


# In[38]:


df3.drop(df3[df3['Category']=='1.9'].index,inplace=True)


# In[39]:


df3.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# In[40]:


plt.figure(figsize=(100,50))
sns.boxplot(x=df3['Category'],y=df3['Rating'])


# In[41]:


df3.isnull().sum()


# In[42]:


x=df3['Rating'].mean()


# # we can impute mean value into the Rating column

# In[43]:


df3['Rating']=df3['Rating'].fillna(x)


# In[44]:


df3.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# #  12

# In[45]:


df3['Size'].unique()


# In[46]:


df3.drop(df3[df3['Size']=='Varies with device'].index,inplace=True)


# In[47]:


# Convert the 'Size' column to numerical format
df3['Size'] = df3['Size'].str.replace('k', 'e+3').str.replace('M', 'e+6').astype(float)

# Check the updated 'Size' column
print(df3['Size'].unique())


# In[48]:


# Assuming df is your DataFrame with the numeric values in scientific notation
df3['Size'] = df3['Size'].apply(lambda x: f"{x:.0f}" if pd.notnull(x) else x)

# Check the updated 'Size' column
print(df3['Size'].unique())


# In[49]:


df3['Size'] = df3['Size'].astype(int)


# In[50]:


sns.scatterplot(x=df3['Size'],y=df3['Rating'])


# In[53]:


df3['Price'].unique()


# In[57]:


df3['Price']=df3['Price'].str.replace('$','')


# In[58]:


df3['Price']=df3['Price'].astype(float)


# In[61]:


avg_prices=df3.groupby('Type')['Price'].mean()


# In[62]:


plt.bar(avg_prices.index,avg_prices.values)


# In[63]:


df3.columns


# In[65]:


df3.head(10)


# In[70]:


df3['Installs']=df3['Installs'].str.replace(',','')
df3['Installs']=df3['Installs'].str.replace('+','')
df3['Installs']=df3['Installs'].astype(int)


# In[73]:


df3_sort=df3.groupby('App')['Installs'].sum().sort_values(ascending=False )


# In[75]:


df3_sort.index[:10]


# In[80]:


plt.figure(figsize=(15,10))
sns.barplot(x=df3_sort.index[:5],y=df3_sort.values[:5])
plt.show()


# In[84]:


df3_sort=df3.groupby('Category')['Installs'].sum().sort_values(ascending=False)


# In[88]:


plt.figure(figsize=(15,10))
sns.barplot(df3_sort.index[:5],df3_sort.values[:5])
plt.show()


# In[89]:


df3.columns


# In[ ]:




