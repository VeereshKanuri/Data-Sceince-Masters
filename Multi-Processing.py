#!/usr/bin/env python
# coding: utf-8

# #1
# Multiprocessing in Python refers to the capability of running multiple processes simultaneously, taking advantage of the full processing power of multi-core CPUs. It allows you to divide a task into smaller subtasks that can be executed independently and concurrently, improving the performance and efficiency of your program.
# 
# Here are a few reasons why multiprocessing is useful in Python:
# 
# Improved Performance: By executing tasks concurrently across multiple processes, multiprocessing can significantly speed up the execution time of CPU-bound operations. Each process runs on a separate core, allowing for parallel computation and better utilization of available resources.
# 
# Parallelism: Python's Global Interpreter Lock (GIL) prevents true parallel execution of threads within a single Python process. However, multiprocessing overcomes this limitation by creating multiple Python processes, each with its own interpreter and memory space. This enables true parallelism and allows for efficient utilization of multiple CPU cores.
# 
# Scalability: Multiprocessing is beneficial when dealing with large datasets or computationally intensive tasks. It allows you to scale your program's performance by distributing the workload among multiple processes, making it easier to handle more significant computational demands

# #2
# Multiprocessing and multithreading are both techniques used to achieve concurrent execution in programming, but they differ in several aspects:
# 
# Execution Model: Multiprocessing involves running multiple processes simultaneously, where each process has its own memory space and runs on a separate CPU core. On the other hand, multithreading involves running multiple threads within a single process, and they share the same memory space.
# 
# Parallelism: Multiprocessing achieves true parallelism since each process runs independently on a separate CPU core, allowing for multiple tasks to be executed simultaneously. In contrast, multithreading typically does not achieve true parallelism due to the Global Interpreter Lock (GIL) in Python, which allows only one thread to execute Python bytecode at a time. However, multithreading can still provide concurrency by leveraging I/O-bound operations or through the use of external libraries that release the GIL.
# 
# Memory: In multiprocessing, each process has its own memory space, which means that variables are not shared between processes by default. Communication between processes usually requires explicit mechanisms like inter-process communication (IPC) or shared memory. In multithreading, threads share the same memory space, which allows them to access and modify the same variables without the need for explicit communication mechanisms.

# In[3]:


#3
#Write a python code to create a process using the multiprocessing module.
import multiprocessing
def fun(name):
    print("hhere is the name of person {}".format(name))
if __name__=="__main__":
    m=multiprocessing.Process(target=fun,args=('veeresh',))
m.start()
m.join()


# #4
# In Python's multiprocessing module, a multiprocessing pool is a high-level abstraction that provides a convenient way to distribute the execution of a function across multiple processes. It manages a pool of worker processes, allowing you to submit tasks for execution and retrieve their results asynchronously.
# 
# The main purpose of using a multiprocessing pool is to parallelize the execution of a function across multiple processes, taking advantage of multi-core CPUs and achieving better performance in CPU-bound tasks. It abstracts away the complexity of manually creating and managing individual processes, making it easier to parallelize computations.

# #5
# To create a pool of worker processes in Python using the multiprocessing module, you can utilize the Pool class. The Pool class provides a high-level interface for managing a pool of worker processes, simplifying the process of parallelizing tasks. Here's an example that demonstrates how to create a pool of worker processes:
# import multiprocessing
# 
# def name(x):
#     print("here is name {}",x)
#     
# if __name__=="__main__":
#     pool= multiprocessing.Pool(processes=5)
#     names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
#     results= pool.map(name,names)
# for i in results:
#     print(i)

# In[ ]:


#6
import multiprocessing
def num(x):
    print(x)
    
if __name__=="__main__":
    pool=multiprocessing.Pool(processes=4)
    list1=[1,2,3,4]
    result=pool.map(num,list1)
for i in result:
    print(i)


# In[ ]:




