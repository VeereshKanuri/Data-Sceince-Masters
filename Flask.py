#!/usr/bin/env python
# coding: utf-8

# #1
# Flask is a popular web framework written in Python. It is designed to be simple, lightweight, and easy to use, making it a popular choice for building web applications and APIs. Here are some key points about Flask and its advantages:
# 
# Minimalistic and Lightweight: Flask follows a "micro" framework philosophy, which means it provides only the essential components needed to build web applications. This minimalistic approach keeps the framework lightweight, easy to understand, and flexible.
# 
# Easy to Learn: Flask has a simple and intuitive API that is easy to grasp, especially for beginners. The framework's simplicity makes it accessible to developers who are new to web development or Python.
# 
# Flexible and Extensible: Flask provides a flexible architecture that allows developers to customize and extend its functionality as needed. You can choose from a wide range of Flask extensions to add features like database integration, authentication, and more.
# 
# Routing and URL Handling: Flask provides a built-in routing system that allows you to map URLs to specific functions, making it easy to define different routes and handle requests.
# 
# Template Engine: Flask includes a template engine called Jinja2, which enables you to create dynamic HTML pages by combining HTML templates with data from your application.

# 
# 
# 
# 
# ![2023-05-20.png](attachment:2023-05-20.png)

# #3
# In Flask, app routing refers to the process of mapping URLs (Uniform Resource Locators) to specific functions in your application. It allows you to define different routes and specify what code should be executed when a user visits a particular URL.
# 
# When a user makes a request to our Flask application, the app routing mechanism determines which function should handle that request based on the URL. This mapping is defined using decorators in Flask.

# 
# Using app routes in Flask offers several benefits:
# 
# Organized Code Structure: App routing allows you to logically structure your code by separating different parts of your application into distinct functions and routes. This improves code organization and maintainability.
# 
# URL Mapping: App routes provide a convenient way to map URLs to specific functions. This enables you to create clean and meaningful URLs for your application's various pages and features.
# 
# Request Handling: By defining app routes, Flask automatically handles incoming requests and dispatches them to the appropriate functions. This eliminates the need for manual request parsing and routing.
# 
# Dynamic Content: App routes enable you to generate dynamic content based on user requests. By incorporating variables and parameters in the routes, you can pass data to the corresponding functions and generate custom responses.

# ![2023-05-20%20%282%29.png](attachment:2023-05-20%20%282%29.png)

# #5
# 
# In Flask, the url_for() function is used for URL building. It generates a URL for a given endpoint (the name associated with a route function) by taking into account the routes defined in the application.
# 
# from flask import Flask
# from flask import request
# from flask import url_for()
# 
# app= Flask(__name__)
# 
# @app.route('/')
# def home():
#     return "home page welcomes you"
#    
# @app.route('/welcome')
# def welcome():
#     return "welcome"
#  
# 
# if __name__ == '__main__':
#         with app.test_request_context():
#         print(url_for('home'))          # Output: /
#         print(url_for('welcome'))       # Output: /welcome      
#         app.run()
