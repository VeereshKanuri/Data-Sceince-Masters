#!/usr/bin/env python
# coding: utf-8

# #1
# open() function is used to open the file 
# ex:
#    synatx: open(file_name,mode='r','w','a',...)
#    file=open('text.txt','r')
# 
# The different modes for opening a file in Python are as follows:
# 
# Read mode ('r'): This is the default mode if no mode is specified. It opens the file for reading. If the file does not exist, it raises a FileNotFoundError. When a file is opened in read mode, you can only read its contents and not modify or write to it.
# 
# Write mode ('w'): It opens the file for writing. If the file exists, its contents are truncated (cleared) before writing. If the file does not exist, a new file is created. When a file is opened in write mode, you can write new data to it or overwrite existing data. If the file already exists and you want to preserve its contents, you should use append mode instead.
# 
# Append mode ('a'): It opens the file for appending. If the file exists, new data is written at the end of the file. If the file does not exist, a new file is created. When a file is opened in append mode, you can only write new data at the end of the file, and the existing contents are not modified.
# 
# Binary mode ('b'): It is used in conjunction with the above modes to open the file in binary mode. Binary mode allows reading or writing raw binary data, such as images or non-text files. For example, 'rb' opens the file in binary mode for reading, while 'wb' opens the file in binary mode for writing.
# 
# Text mode ('t'): It is the default mode and can be omitted. It opens the file in text mode, which means the data is treated as text. Text mode is used for reading or writing regular text files. For example, 'rt' opens the file in text mode for reading, while 'wt' opens the file in text mode for writing   
# 

# #2
# #close() function is used to close the file.
# Incomplete data: When you write data to a file, the operating system often stores it in memory instead of immediately writing it to the disk. If you don't close the file properly, the data may stay in memory and not be saved to the file. This can result in the file having incomplete or missing data.
# 
# Resource leak: When you open a file, the operating system assigns certain resources to handle the file operations. These resources include memory and file descriptors. If you don't close the file correctly, these resources may not be released, causing your program to consume more memory than necessary and potentially slowing down your program's performance.
# 
# Locking and availability: Sometimes, when a file is open, it can be "locked" or marked as unavailable for other processes or programs to access. If you don't close the file, it might remain locked, preventing other parts of your program or other programs from reading or writing to the file. This can cause conflicts and issues if multiple processes need to work with the same file.
# 

# In[23]:


#3
with open('text.txt','w') as f:
    f.write("""Hello, this is line 1.
This is line 2.
And this is line 3.
""")
with open('text.txt','r') as f:
    print(f.read())


# In[24]:


#4
# Example using read()
with open('text.txt', 'r') as file:
    contents = file.read()
    print(contents)
# Example using readline()
with open('text.txt', 'r') as file:
    line = file.readline()
    print(line)
# Example using readlines()
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)


# # 5
# 
# he with statement in Python is used in conjunction with the open() function to provide a convenient and efficient way of working with files. The with statement ensures that the file is properly opened and closed, even if an exception occurs during the execution of the code block. This helps to maintain code readability, improve resource management, and handle file-related errors effectively.
# 
# Here are the advantages of using the with statement with open():
# 
# Automatic file closing: When you use the with statement, you don't need to explicitly call the close() method on the file object. The with statement takes care of automatically closing the file once the code block is exited, regardless of whether an exception occurs or not. This eliminates the need to remember to close the file and reduces the risk of resource leaks.
# 
# Exception handling: If an exception occurs within the with block, the with statement ensures that the file is still closed properly. It automatically handles any exceptions and guarantees that the __exit__() method of the file object is called, which includes closing the file. This helps to prevent file-related errors and ensures that the file is closed safely, even in exceptional circumstances.
# 
# Cleaner code and improved readability: The with statement provides a clean and readable way to work with files. By encapsulating the file operations within the with block, it becomes clear which part of the code is responsible for file handling. This improves code readability and makes it easier for other developers to understand and maintain the code.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# # 6
# write(): The write() function is used to write a string or a sequence of characters to a file. It appends the content to the existing file or creates a new file if it doesn't exist.
# 
# # Example using write()
# with open('output.txt', 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a sample text.\n')
# writelines(): The writelines() function is used to write multiple lines to a file. It takes a sequence (such as a list or tuple) of strings and writes each string as a separate line in the file.
# # Example using writelines()
# lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
# 
# with open('output.txt', 'w') as file:
#     file.writelines(lines)
# 

# In[ ]:




