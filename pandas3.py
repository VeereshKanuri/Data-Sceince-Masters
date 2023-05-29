#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})


# In[11]:


#1
df.loc[1]

count=1

for  i in df.iterrows():
    if count==2:
        print(i)
    count=count+1


# #2
# 
# loc: The loc function is primarily label-based. It is used to access data by using the labels or indices of rows and columns. With loc, you can specify the row and column labels to retrieve specific data.
# 
# Example: df.loc[row_label, column_label]
# 
# The labels can be integers, strings, or boolean values. When using loc, both the start and end labels are inclusive.
# 
# iloc: The iloc function is primarily integer position-based. It is used to access data by using integer indices of rows and columns. With iloc, you can specify the row and column positions (0-based index) to retrieve specific data.
# 
# Example: df.iloc[row_index, column_index]
# 
# The indices are always integers. When using iloc, the start position is inclusive, but the end position is exclusive.

# In[25]:


new_df=df.reindex([3,0,1,2])
print(new_df.loc[2])
print(new_df.iloc[2])

#yes there is difference between both the outputs.for iloc output is based on index based and for loc output is based on position based.


# In[27]:


import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


# In[39]:


#4
lis1=list(df1.columns)
mean_lis=[]
for i in lis1:
    mean_lis.append(df1[i].mean())
print(mean_lis)
df1["column_2"].std()  


# In[ ]:


#5
df1.loc[2,'column_2']='veer'
df1['colum_2'].mean()
#TypeError: unsupported operand type(s) for +: 'float' and 'str'


# #6
# 
# windows functions are sued to perform calculations over a sliding or rolling window of data in series.
# #There are several types of window functions 
# 
# 1.Rolling functions()
# these functions operate on a defined window of consecutive data points and calculate statistics such as mean,sum,maximum etc.
# ex:
# 
# import pandas as pd
# import numpy as np
# 
# # Create a DataFrame with random data
# 
# df = pd.DataFrame(np.random.randint(1, 10, size=(10, 1)), columns=['Value'])
# 
# df["rolling_mean"]= df["Value"].rolling(window=3).mean()
# 
# 2.expanding functions()
# These functions expand the window size over time and calculate statistics on the accumulated data. The window starts with a minimum number of data points and progressively grows as new data points are included. Commonly used expanding functions include expanding, expanding_mean, expanding_sum, expanding_min, expanding_max, expanding_std, etc.
# 
# df = pd.DataFrame(np.random.randint(1, 10, size=(10, 1)), columns=['Value'])
# 
# df["Value"].expanding().sum()
# 
# 3.Exponentially wreighs()
# Exponentially Weighted Functions: These functions apply weights to the data points within the window, with more recent data points given higher weights. They are commonly used to calculate moving averages or exponentially weighted statistics. Some commonly used exponentially weighted functions include ewm, ewm_mean, ewm_sum, ewm_min, ewm_max, ewm_std, etc.
# 
# df = pd.DataFrame(np.random.randint(1, 10, size=(5, 1)), columns=['Value'])
# 
# # Calculate the exponentially weighted average with a decay factor of 0.5
# 
# df['EWMA'] = df['Value'].ewm(alpha=0.5).mean()

# In[67]:


#7
current_date=pd.datetime.now()
current_year=current_date.year
print(current_year)
current_month=current_date.month
print(current_month)


# In[8]:


#8
from datetime import datetime, timedelta

date1_str ="2022-09-20"
date2_str ="2023-03-30"
date1=datetime.strptime(date1_str,"%Y-%m-%d")
date2=datetime.strptime(date2_str,"%Y-%m-%d")
time_diff=date2-date1
days=time_diff.days
hours=time_diff.seconds//3600
minutes = (time_diff.seconds % 3600) // 60
print(time_diff)


# In[ ]:


#9
import pandas as pd

# Prompt the user to enter the file path, column name, and category order
file_path = input("Enter the file path: ")
column_name = input("Enter the column name to convert: ")
category_order = input("Enter the category order (comma-separated values): ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert the specified column to categorical data type with the specified category order
category_order_list = [category.strip() for category in category_order.split(',')]
df[column_name] = pd.Categorical(df[column_name], categories=category_order_list, ordered=True)

# Sort the DataFrame based on the specified column
sorted_df = df.sort_values(column_name)

# Display the sorted data
print(sorted_df)


# In[ ]:


#10
import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to enter the file path
file_path = input("Enter the file path: ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Group the data by product category and date, and calculate the total sales
grouped_df = df.groupby(['Category', 'Date'])['Sales'].sum().unstack()

# Plot the stacked bar chart
grouped_df.plot(kind='bar', stacked=True)

# Set the chart title and labels
plt.title('Sales by Product Category Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')

# Display the chart
plt.show()


# In[ ]:


#11
import pandas as pd

# Prompt the user to enter the file path of the CSV file
file_path = input("Enter the file path of the CSV file containing the student data: ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Calculate the mean, median, and mode of the test scores
mean = df['Test Score'].mean()
median = df['Test Score'].median()
mode = df['Test Score'].mode()

# Create a table to display the results
results_table = pd.DataFrame({'Statistic': ['Mean', 'Median', 'Mode'],
                              'Value': [mean, median, mode]})

# Display the table
print(results_table)

