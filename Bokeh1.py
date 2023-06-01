#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import bokeh.io


# In[2]:


import bokeh.plotting


# In[3]:


from bokeh.plotting import figure,output_file,show


# In[4]:


bokeh.io.output_notebook()


# In[10]:


p=figure()


# In[11]:


p.circle(x=[1, 2, 3], y=[4, 2, 5])


# In[7]:


show(p)


# In[13]:


p.xaxis.axis_label="X-AXIS"
p.yaxis.axis_label="Y-AXIS"


# In[14]:


show(p)


# # 2
# 
# GLYPHS
# 

# Glyphs in Bokeh are visual markers used to represent data on a plot. They can be simple shapes like circles, squares, or lines, or more complex markers like triangles or asterisks. Glyphs allow you to visually encode and display your data points in a meaningful way.
# 
# To add glyphs to a Bokeh plot, you need to use the appropriate glyph method provided by the figure object. Here's an example that demonstrates how to add circle glyphs to a scatter plot:

# In[15]:


from bokeh.plotting import figure, show

# Create a figure object
plot = figure()

# Add circle glyphs
plot.circle(x=[1, 2, 3], y=[4, 2, 5], size=10, fill_color='blue', line_color='black')

# Display the plot
show(plot)


# In[26]:


plot.circle(x=[1,2,3,4],y=[2,3,4,5],size=2,fill_color="blue",line_color="orange")


# In[27]:


show(plot)


# In[1]:


#3
import bokeh.io
import bokeh.plotting
from bokeh.plotting import figure,show
from bokeh.sampledata.iris import flowers


# In[2]:


flowers


# In[3]:


p=figure()


# In[4]:


p.circle(flowers['petal_length'],flowers['petal_width'])


# In[7]:


p.xaxis.axis_label="petal_length"
p.yaxis.axis_label="petal_width"


# In[8]:


show(p)


# #4
# The Bokeh server is a key component of Bokeh that allows you to create interactive plots and applications that can be updated in real time. It enables you to build dynamic web-based visualizations and dashboards by combining the power of Bokeh with the capabilities of a web server.
# 
# When you use the Bokeh server, the plot is served as a web application that runs on a server and can be accessed by multiple users simultaneously. Users can interact with the plot, and any changes they make trigger updates to the plot in real time for all connected clients.

# To embed a Bokeh plot into a web page or dashboard using Flask or Django, you can follow these general steps:
# 
# Generate the Bokeh plot and save it as an HTML file.
# 
# python
# Copy code
# from bokeh.plotting import figure, output_file, show
# 
# # Create a figure and add glyphs
# plot = figure()
# plot.circle([1, 2, 3], [4, 2, 5])
# 
# # Specify the output file
# output_file("bokeh_plot.html")
# 
# # Save the plot as an HTML file
# show(plot)
# This code creates a Bokeh plot, adds glyphs to it, and saves it as an HTML file using the output_file function.
# 
# In your Flask or Django application, create a view or route that renders the HTML file containing the Bokeh plot.
# 
# For Flask:
# 
# python
# Copy code
# from flask import Flask, render_template
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def index():
#     return render_template('index.html')
# 
# if __name__ == '__main__':
#     app.run()
# For Django:
# 
# python
# Copy code
# from django.shortcuts import render
# 
# def index(request):
#     return render(request, 'index.html')
# In both cases, the index function is responsible for rendering the index.html template.
# 
# Create an HTML template file that includes the necessary JavaScript and CSS dependencies for Bokeh.
# 
# For Flask, create an index.html file with the following content:
# 
# html
# Copy code
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Bokeh Plot</title>
#     {{ bokeh_css }}
# </head>
# <body>
#     <div>
#         {{ bokeh_plot }}
#     </div>
#     {{ bokeh_js }}
# </body>
# </html>
# For Django, create a index.html file within your template directory with the same content.
# 
# Modify the Flask or Django view to pass the necessary script and div tags to the template.
# 
# For Flask:
# 
# python
# Copy code
# @app.route('/')
# def index():
#     with open('bokeh_plot.html', 'r') as f:
#         bokeh_plot = f.read()
# 
#     return render_template('index.html', bokeh_plot=bokeh_plot)
# For Django:
# 
# python
# Copy code
# def index(request):
#     with open('bokeh_plot.html', 'r') as f:
#         bokeh_plot = f.read()
# 
#     return render(request, 'index.html', {'bokeh_plot': bokeh_plot})
# In both cases, we read the contents of the Bokeh plot HTML file and pass it to the index.html template.
# 
# Start your Flask or Django application, and visit the specified URL to see the embedded Bokeh plot.
# 
# With Flask, the application is started with app.run(). With Django, you need to run the manage.py file with python manage.py runserver

# In[ ]:




