#!/usr/bin/env python
# coding: utf-8

# #1
# MongoDB is a popular NoSQL (non-relational) database management system that provides a flexible and scalable approach to storing and retrieving data. Unlike traditional SQL databases, which use tables with fixed schemas and relationships, MongoDB stores data in flexible documents using a format called BSON (Binary JSON)
# 
# Non-relational databases, or NoSQL databases, offer a different approach to data management compared to SQL databases. They are designed to handle large volumes of unstructured or semi-structured data and provide high scalability and performance. NoSQL databases typically do not enforce rigid schema requirements, allowing for more flexibility in handling evolving data structures. They can handle a variety of data types, including documents, key-value pairs, graphs, or time series.
# 
# MongoDB is preferred over SQL databases in several scenarios:
# 
# Flexible and evolving data structures: When dealing with data that doesn't fit well into a fixed schema, MongoDB's document model allows for easy handling of evolving data structures and dynamic schema changes.
# 
# Scalability and performance: MongoDB's distributed architecture and support for horizontal scaling make it suitable for handling high-traffic applications and big data workloads. It can efficiently distribute data across multiple servers, providing improved performance and scalability.
# 
# Rapid development and iteration: MongoDB's flexible schema and document-oriented nature make it well-suited for agile development processes. It enables developers to quickly prototype, iterate, and adapt their data models as needed without strict schema migrations.

# #2
# FEATURES OF MONGODB
# 
# Document-Oriented: MongoDB stores data in flexible and self-describing JSON-like documents called BSON. This document-oriented approach allows for easy storage and retrieval of data without the need for rigid table structures found in traditional relational databases.
# 
# Scalability and High Performance: MongoDB is designed to scale horizontally, meaning it can handle large volumes of data and high traffic loads by distributing data across multiple servers or clusters. This scalability ensures efficient performance even as your application and data grow.
# 
# Flexible Schema: MongoDB's schema is dynamic, allowing documents within a collection to have different structures and fields. This flexibility allows you to evolve your data model over time without requiring expensive schema migrations, making it well-suited for agile development and fast iteration.
# 
# High Availability and Fault Tolerance: MongoDB supports automatic replica set creation, which involves maintaining multiple copies of your data across different servers. This provides high availability and fault tolerance, ensuring that your data remains accessible even if one server goes down.
# 
# Querying and Indexing: MongoDB offers a powerful and expressive query language that supports a wide range of operations, including filtering, sorting, and aggregation. It also provides indexing capabilities to improve query performance by efficiently retrieving specific data subsets.

# In[9]:


#3
import pymongo
 
client=pymongo.MongoClient("mongodb+srv://veeresh2809:veeresh@cluster0.tk84sd1.mongodb.net/?retryWrites=true&w=majority") 

db=client['DataBase']

coll= db['Collection']

data = {
    'name': 'veeresh',
    'age': 20,
    'email': 'veeresh2809@gmail.com'
}

result = coll.insert_one(data)

documents = coll.find()
for document in documents:
    print(document)







# In[12]:


#4
data = {
    'name': 'veeresh',
    'age': 20,
    'email': 'veeresh2809@gmail.com'
}

coll.insert_one(data)

data_many = [
    {
        'name': 'Bob',
        'age': 28,
        'email': 'bob@example.com'
    },
    {
        'name': 'Charlie',
        'age': 30,
        'email': 'charlie@example.com'
    },
    {
        'name': 'David',
        'age': 35,
        'email': 'david@example.com'
    }
]

coll.insert_many(data_many)

for i in coll.find_one():
        print(i)
for i in coll.find():
    print(i)
    




# In[13]:


#5

#The find() method in MongoDB is used to query a database collection and retrieve documents that match specific criteria. It allows you to specify filtering conditions, sorting options, projection of specific fields, and more.

data = {
    'name': 'veeresh',
    'age': 20,
    'email': 'veeresh2809@gmail.com'
}

for i in coll.find():
    print(i)


# In[14]:


#6

#The sort() method in MongoDB is used to sort the result of a query based on specified sorting criteria.
#It allows you to sort documents in ascending or descending order based on one or more fields

documents = [
    { 'name': 'Alice', 'age': 25 },
    { 'name': 'Bob', 'age': 30 },
    { 'name': 'Charlie', 'age': 28 },
    { 'name': 'David', 'age': 35 }
]

coll.insert_many(documents)

sort_ord=coll.find().sort('age',-1)

for i in sort_ord:
    print(i)


# #7
# delete_one(filter):
# 
# This method is used to delete a single document that matches a specific filter or criteria.
# 
# delete_many(filter):
# 
# This method is used to delete multiple documents that match a specific filter or criteria.
# 
# drop():
# 
# This method is used to drop or delete an entire collection from a database.
# It removes the collection and all its documents, indexes, and associated data.
# 

# In[ ]:




