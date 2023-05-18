#!/usr/bin/env python
# coding: utf-8

# #1
# Multithreading in Python refers to the concurrent execution of multiple threads within a single process. A thread is a separate flow of execution within a program that can run independently, allowing multiple tasks to be performed simultaneously
# Threads are used to achieve parallelism or concurrent execution, particularly when dealing with tasks that can be executed independently or when responsiveness is crucial. By utilizing multiple threads, a program can perform multiple operations concurrently, improving overall performance and efficiency.
# The threading module is commonly used to handle threads in Python. It provides a high-level interface for creating, managing, and synchronizing threads. The threading module allows you to define and start new threads, control their execution, communicate between threads, and handle synchronization mechanisms like locks, events, and semaphores.

# #2
# the threading module in python is used to handle the threads and provivde high level interface for creating and managing threads.it offers various functions to interact with threads .
# activeCount():
# 
# The activeCount() function returns the number of Thread objects currently alive.
# It helps in determining the total number of active threads at a given point in the program.
# It can be useful for monitoring the progress or status of threads during execution.
# currentThread():
# 
# The currentThread() function returns the currently executing Thread object.
# It allows you to obtain a reference to the thread from within the code being executed by that thread.
# This function is useful for identifying the thread that is currently running and accessing its properties or performing operations on it.
# 
# enumerate():The enumerate() function returns a list of all Thread objects currently alive.
# It provides a way to iterate over all active threads and access their properties or perform operations on them.
# It is useful for tasks such as monitoring or managing the state of threads, or performing actions on all active threads.

# #3
# import threading 
# def fun():
#     print("hello")
# 
# my_thread =threading.Thread(target=fun)
# my_thread.start()
# print("hi")
# print("is my thread alive",my_thread.is_alive())
# my_thread.join()
# print("is my thread alive",my_thread.is_alive())
# 
# 
# run():
# 
# The run() method is the entry point for the thread's activity or the code that will be executed when the thread starts.
# It represents the task or functionality that you want the thread to perform.
# When a thread is created, you can define the task to be executed by overriding the run() method of the Thread class or passing a callable target function to the thread.
# The run() method is automatically called when you start the thread using the start() method.
# 
# start():
# 
# The start() method is used to start the execution of a thread.
# It initializes the thread's internal structures, assigns a new system-level thread, and calls the thread's run() method.
# The start() method must be called only once per thread object. If you try to start a thread that has already been started or is currently running, it will raise a RuntimeError.
# 
# join():
# 
# The join() method is used to wait for a thread to complete its execution.
# It blocks the calling thread until the thread on which it's called has finished.
# When you call join() on a thread, it waits until the thread's run() method or target function has finished executing.
# The calling thread will not proceed beyond the join() call until the joined thread has terminated.
# Optionally, you can specify a timeout parameter to limit the waiting time for the thread to finish.
# 
# 
# The isAlive(): method is used to check whether a thread is currently executing or alive.
# It returns True if the thread is still running, and False otherwise.
# The thread is considered alive from the moment it is started using the start() method until it completes its task and terminates.
# This method is useful when you want to check the status of a thread and take appropriate actions based on its execution stat

# In[1]:


#4
import threading

def fun(n):
    print(f"Square of {n}: {n**2}")

def fun1(n):
    print(f"Cube of {n}: {n**3}")

t1 = [threading.Thread(target=fun, args=(p,)) for p in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
t2 = [threading.Thread(target=fun1, args=(k,)) for k in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

for thread in t1:
    thread.start()

for thread in t2:
    thread.start()

for thread in t1:
    thread.join()

for thread in t2:
    thread.join()


# #5
# Advantages of Multithreading ():
# 
# Faster execution: Multithreading allows different parts of a program to work together at the same time, making the program run faster.
# 
# Better resource utilization: Multithreading helps use the computer's resources more efficiently, making the program run more smoothly.
# 
# Easier organization: Multithreading divides a program into smaller parts, making it easier to understand and manage.
# 
# Simpler program flow: Multithreading makes it easier to write programs that do multiple things at once, making the program flow more smoothly.
# 
# Disadvantages of Multithreading ():
# 
# More complexity: Multithreading can make the program more complex and harder to understand, leading to potential errors.
# 
# Difficult debugging: Multithreading can make it harder to find and fix problems in the program.
# 
# More memory usage: Multithreading uses more memory because each thread needs its own resources.
# 
# Limited scalability: Multithreading may not always make a program faster, especially for certain tasks that don't benefit from it.

# #6
# Deadlock:
# Imagine you have two friends, Alice and Bob, who each have a key to their respective rooms but need the other person's key to enter. They both enter the hallway and realize they can't enter their rooms because they're waiting for the other person's key. They end up stuck in the hallway, unable to proceed. This situation is similar to a deadlock.
# In programming, deadlocks can occur when two or more threads are waiting for each other to release resources. For example, Thread A holds Resource X and is waiting for Resource Y, while Thread B holds Resource Y and is waiting for Resource X. As a result, both threads are stuck, and the program cannot make progress.
# 
# Race Condition:
# Imagine you and your friend are writing messages on a whiteboard simultaneously. You both start with a blank whiteboard and write your messages one line at a time. However, since you're not coordinating with each other, you may end up overwriting each other's messages or getting incomplete sentences. The final result depends on the timing and order of your writing, creating a race conditio
