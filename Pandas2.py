#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


#1

df=pd.read_csv('train.csv')
df.head()
df.info()
df.describe()
df.groupby('Sex').mean()


# In[44]:


#2

import pandas as pd

def reindex_dataframe(df):
    new_index = pd.RangeIndex(start=1, stop=len(df)*2, step=2)  # Create a new index with desired start and increment
    df = df.set_index(new_index)  # Set the new index on the DataFrame
    
    return df

new_df = reindex_dataframe(df)
print(new_df)


df= pd.DataFrame({'A':[1,2,3],'B':[3,4,5],'C':[8,9,10]})


# In[58]:


#3
def fun(df):
    x=0
    count=0
    for index,rows in df.iterrows():
        if count<3:
            rows["Values"]
     
    
    


# In[60]:


#4
import pandas as pd

def count_words(df):
    # Create a new column 'Word_Count' by applying a lambda function to each row in the 'Text' column
    df['Word_Count'] = df['Text'].apply(lambda x: len(str(x).split()))

    # Return the updated DataFrame
    return df


# #5
# DataFrame.size(): This method returns the total number of elements in the DataFrame. It calculates the size by multiplying the number of rows (DataFrame.shape[0]) with the number of columns (DataFrame.shape[1]). The size() method returns a single integer value representing the total number of elements in the DataFrame.
# 
# DataFrame.shape(): This method returns a tuple containing the dimensions of the DataFrame. The tuple consists of two elements: the number of rows and the number of columns, respectively. It provides the shape of the DataFrame in the format 

# #6
# pd.read_excel

# In[68]:


#7
def fun(df):
    df=df['new_Email']=df["Email"].str.split('@').str[0]
    return df


# In[91]:


#8
def select_rows(df):
    selected_rows = df[(df['A'] > 5) & (df['B'] < 10)]
    return selected_rows


# In[96]:


#9
def fun(df):
    mean=df['Values'].mean()
    median=df['Values'].median()
    std=df['Values'].std()
    return f"mean,median,std of values  column {mean} {median} {std}"
    


# In[101]:


#10
df=pd.DataFrame({'Date':["2023-01-01","2023-01-02","2023-01-03"]})
def fun(df):
    df["new_date"]=pd.to_datetime(df["Date"])
    df["weekday"].dt.weekday
    return df


# In[104]:


#11
def select_rows(df):
    # Convert 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter rows based on date range
    selected_rows = df[(df['Date'] >= '2023-01-01') & (df['Date'] <= '2023-01-31')]
    
    return selected_rows


# #12
# The first and foremost library that needs to be imported to use the basic functions of pandas is the pandas library itself
