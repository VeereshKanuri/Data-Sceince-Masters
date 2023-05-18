#!/usr/bin/env python
# coding: utf-8

# #1
# 
# A database is an organized collection of structured data that is stored and managed on a computer system. It allows users to efficiently store, retrieve, manipulate, and analyze data for various purposes. Databases are commonly used in applications and systems that require the management of large amounts of data
# 
# SQL and NoSQL are two different types of database management systems (DBMS) that have distinct approaches to storing and retrieving data:
# 
# SQL Databases (Relational Databases):
# SQL, which stands for Structured Query Language, is a language used to communicate with relational databases. Relational databases organize data into tables, where each table consists of rows and columns. They follow a predefined schema that defines the structure and relationships between tables.
# Popular SQL databases include MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.
# 
# NoSQL Databases (Non-Relational Databases):
# NoSQL databases, as the name suggests, do not adhere to a fixed schema and are designed to handle unstructured and semi-structured data. They offer flexibility in terms of data models and are often used for handling large-scale distributed data.

# #2
# 
# DDL stands for Data Definition Language, which is a subset of SQL (Structured Query Language). DDL statements are used to define and manage the structure of a database, including creating, modifying, and deleting database objects such as tables, indexes, and constraints.
# ex:
# CREATE:
# The CREATE statement is used to create a new database object, such as a table, index, or view. It specifies the name of the object and defines its structure and characteristics.
# CREATE TABLE Employees (
#     ID INT PRIMARY KEY,
#     Name VARCHAR(50),
#     Salary DECIMAL(10,2)
# );
# 
# 
# DROP:
# The DROP statement is used to delete an existing database object, such as a table, index, or view. It permanently removes the object and its associated data from the database.
# 
# DROP TABLE Employees;
# 
# 
# ALTER:
# The ALTER statement is used to modify the structure of an existing database object, such as adding or dropping columns from a table, modifying constraints, or renaming an object.
# 
# ALTER TABLE Employees
# ADD department VARCHAR(50
# 
# TRUNCATE:
# The TRUNCATE statement is used to delete all data from an existing table, while preserving the table structure. It removes all rows from the table but keeps the table itself intact.
# 
# TRUNCATE table Employees

# #3
# 
# DML stands for Data Manipulation Language, which is a subset of SQL (Structured Query Language). DML statements are used to manipulate the data stored in a database. They allow you to insert, update, and delete records in database tables.
# INSERT:
# 
# The INSERT statement is used to insert new records into a table. It allows you to specify the values to be inserted for each column or select values from another table.
# Example: Inserting a new record into the "Employees" table with values for the ID, Name, and Salary columns:
# 
# INSERT INTO Employees (ID, Name, Salary)
# VALUES (1, 'John Doe', 5000.00);
# 
# UPDATE:
# 
# The UPDATE statement is used to modify existing records in a table. It allows you to change the values of one or more columns based on specified conditions.
# Example: Updating the salary of the employee with ID 1 in the "Employees" table:
# 
# UPDATE Employees
# SET Salary = 6000.00
# WHERE ID = 1;
# 
# DELETE:
# The DELETE statement is used to delete one or more records from a table based on specified conditions.
# EX:
#  Deleting the employee with ID 1 from the "Employees" table:
#  
#  DELETE FROM Employees
#  where ID=1;
#  

# #4
# 
# DQL stands for Data Query Language, which is a subset of SQL (Structured Query Language). DQL statements are used to retrieve and query data from a database. The most commonly used DQL statement is SELECT, which allows you to retrieve specific data from one or more tables:
# 
# SELECT:
# The SELECT statement is used to retrieve data from one or more tables in a database. It allows you to specify the columns you want to retrieve, the table(s) you want to query, and optional conditions to filter the results. It can also include various clauses such as WHERE, ORDER BY, GROUP BY, JOIN, and more to further refine the query results.
# 
# Example: Retrieving the names of all employees from the "Employees" table:
# SELECT Name
# FROM Employees;
# 

# #5
# 
# A primary key is a column or a set of columns in a database table that uniquely identifies each record within that table. It serves as a unique identifier for each row, ensuring that there are no duplicate values. A primary key constraint enforces the uniqueness and non-nullability of the primary key column(s).
# 
# A foreign key is a column or a set of columns in a database table that refers to the primary key of another table. It establishes a relationship between two tables by enforcing referential integrity. The foreign key constraint ensures that the values in the foreign key column(s) match the values in the primary key column(s) of the referenced table or are NULL.

# In[ ]:


#6

import mysql.connector

# Establishing the connection
mydb = mysql.connector.connect(
    host="localhost",
    user="veeresh",
    password="veeru@2809",
    database="veer1"
)

# Creating a cursor object
cursor = mydb.cursor()

#creating a database
cursor.execute("CREATE DATABASE TABLE1")

#Creating a table in database
cursor.execute("CREATE TABLE employees")

# Executing a query
cursor.execute("SELECT * FROM employees")

# Fetching the results
results = cursor.fetchall()

# Displaying the results
for row in results:
    print(row)

# Closing the connection
mydb.close()

#cursor(): The cursor() method creates a cursor object that allows you to execute SQL statements and interact with the database.
#The cursor acts as a handle or pointer to the result set returned by the query.

#execute(): The execute() method is used to execute SQL statements or queries. 
#It takes the SQL statement as a parameter and sends it to the database for execution. 
#The execute() method can be used with placeholders for parameterized queries.


# #7
# The general order of execution for SQL clauses in an SQL query is as follows:
# 
# SELECT: The SELECT clause specifies the columns to be retrieved from the database.
# 
# FROM: The FROM clause indicates the table(s) from which the data will be retrieved.
# 
# WHERE: The WHERE clause filters the rows based on specified conditions.
# 
# GROUP BY: The GROUP BY clause is used to group the rows based on one or more columns.
# 
# HAVING: The HAVING clause filters the grouped rows based on specified conditions.
# 
# ORDER BY: The ORDER BY clause is used to sort the result set based on one or more columns.
# 
# LIMIT/OFFSET: The LIMIT and OFFSET clauses are used to restrict the number of rows returned or skip a certain number of rows.
