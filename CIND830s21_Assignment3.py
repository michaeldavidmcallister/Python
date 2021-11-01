#!/usr/bin/env python
# coding: utf-8

# ## CIND830 - Python Programming for Data Science  
# ### Assignment 3 (10% of the final grade) 
# ### Due on Jun 16, 2021 11:59 PM

# *****
# This is a Jupyter Notebook document that extends a simple formatting syntax for authoring HTML and PDF.
# Review [this](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) website for more details on using Jupyter Notebook.
# 
# Use the JupyterHub server on the Google Cloud Platform, provided by your designated instructor, for this assignment. 
# Ensure using **Python 3.7.6** release then complete the assignment by inserting your Python code wherever seeing the string "#INSERT YOUR ANSWER HERE."
# 
# When you click the `File` button, from the top navigation bar, then select `Export Notebook As ...`,
# a document (PDF or HTML format) will be generated that includes
#  both the assignment content and the output of any embedded Python code chunks.
# 
# Using [these](https://www.ryerson.ca/courses/students/tutorials/assignments/) guidelines,
# submit **both** the IPYNB and the exported file (PDF or HTML).
# Failing to submit both files will be subject to mark deduction.

# ### Question 1 **[100 pts]**: 
# 
# Write a class **List** that can be initialized with a list of positive real numbers. 
# 
# **Note. Do not use any library for any part of the code. Importing any library will result in deduction of points.** 
#     
# 1. Users of the class should be able to initialize an object of the **List** class with a list of numbers. Name the list as *items*. Other than creating *items* list in the constructor, you may need to add more instructions to fulfill requirements of this task. **(20 Points)**
#     
# 2. Implement a *sort* method as a member of the **List** class. The sort method should sort the *items* in ascending order. Use insertion sort algorithm for this task. **(10 Points)**
#     
# 3. Implement a *contains* method as a member the **List** class. It should take a parameter x. If x is in the *items*, the *contains* method should return True otherwise False. Use binary search algorithm to implement this method. **(10 Points)**
#         
# 4. Implement seperate methods as members of the **List** class to calculate measures of central tendency and spread i.e. *mean*, *median*, *mode*, *iqr*, *stdev*, *variance*. Check the formulas from any standard statistics text book.  Note: The idr method will calculate quartile 1 and 3. Use the nearest point if the quartile position in in between two points. e.g. 3 for 3.49 and 4 for 3.51. **(30 Points)**
#     - [stdev, variance example](https://en.wikipedia.org/wiki/Standard_deviation#Basic_examples)
#     - [mean, median and mode example](https://en.wikipedia.org/wiki/Mode_(statistics)#Mode_of_a_sample)
#         - *mode* method should provide mode value and its frequency as a tuple. e.g. The mode output of [1, 2, 2, 2, 3, 4, 5] will be (2, 3)
#     - [iqr example](http://web.mnstate.edu/peil/MDEV102/U4/S36/S363.html)
#     
# 
# 5. An outlier is an unusual data element that might be caused by errors or incorrect data entry. Implement an *outliers* method as a member of the **List** class. It shoud return a list of items that are outliers according to the following formula. **(10 Points)**
#         
#     - item > 1.5 x IQR  + 3rd Quartile OR item < 1st Quartile - 1.5  x IQR
#     - Example as follows
# ```py
# a_list = List(items=[5,3,7,3,6,4,5,8,2,9,3,4,11,-2])
# a_list.outliers()
# [-2, 11]
# ```
# 
# 6. Implement a *stats* method as a member of the **List** class that will print the statistics of data in the *items* list in a nice format. Example as follows. **(10 Points)**
# ```
# a_list = List(items=[5,3,7,3,6,4,5,8,2,9,3,4,11,-2])
# a_list.stats()
# n		: 14
# min		: -2
# max		: 11
# mean	: 4.857142857142857
# median	: 4.5
# mode	: (3, 3)
# stdev	: 11.7351730159502
# q1		: 3
# q3		: 6
# iqr		: 3 
# ```
# 
# 7. Users of the **List** class should not be able to invoke any method except, *outliers*, *contains* and *stats*. **(Bonus Question)(10 Points)**

# In[1]:


class List:
    '''
    Initialize List object with a list of numbers.
    Name is list as items
    '''
    def initializer():
        pass
    '''
    sort method: 
        sort items in ascending order 
        using insertion sort algorithm
    '''    
    def sort():
        pass
    '''
    contains method: 
        search a given item x in items list 
        using binary search algorithm
    '''
    def contain():
        pass
    '''
    A method to calculate mean of the items in the list.
    '''
    def mean():
        pass
    '''
    A method to calculate median of the items in the list.
    '''
    def median():
        pass
    '''
    A method to calculate mode of the items in the list.
    '''
    def mode():
        pass
    '''
    A method to calculate variance and standard deviation
    of the items in the list.
    '''
    def var():
        pass
    '''
    A method to calculate iqr
    of the items in the list.
    '''
    def iqr():
        pass
        
    '''
    A method to detect outliers 
    in the items in the list.
    '''
    def outliers():
        pass
    '''
    A method to print statistics
    of the items in the list.
    '''
    def stats():
        pass


# ### Question 2 **[30 pts]**:
# 
# 
# 

# Consider a ride sharing scenario where we have a line of kids waiting in front of a ride. In what order should the ride be allocated to each kid.? 
# - Implement a Round Robin Scheduling algorithm using queues in Python that will allow equal share of ride time to all the kids.
# - *required_time*: Each kid may like to ride for a given duration of time. 
# - *time_quantum*: Ride will be given to each kid for maximum 2 minutes and then to the next kid.
# - After taking the ride for 2 minutes, if the kid still want more time, he/she will be moved to a waiting queue.

# Answer the following questions:
# - Report the time each kid took to finish the ride
# - Report wait times of each process in the queue
# 

# $$\text{Wait time} = \text{End time} - \text{Arrival Time} - \text{Required Time}$$

# >Kid ID | Arrival Time | Required Time |
# >--- | --- | ---
# >K1 | 0 | 4
# >K2 | 1 | 3
# >K3 | 2 | 2
# >K4 | 3 | 1
# 

# In[2]:


# use deque class for implementing the solution
from collections import deque
time_quantum = 2


# In[3]:


# The Kid class will encapsulate arrival, required and ride time for a kid
class Kid:
    def __init__(self, name, arrival_time, required_time):
        self.name = name
        self.arrival_time = arrival_time
        self.required_time = required_time
        self.time_processed = 0
    def __repr__(self):
        return self.name


# In[4]:


# Scenario: 4 kids with given arrival time and required ride time 
k0 = Kid(name='K1', arrival_time= 0, required_time=4)
k1 = Kid(name='K2', arrival_time= 1, required_time=3)
k2 = Kid(name='K3', arrival_time= 2, required_time=2)
k3 = Kid(name='K4', arrival_time= 3, required_time=1)
kids_in_line = [k0, k1, k2, k3]


# In[5]:


# dicionaries to keep track of end and wait times
end_times = {kid.name:0 for kid in kids_in_line}
wait_times = {kid.name:0 for kid in kids_in_line}


# In[6]:


for t in range(11):
  ### CODE HERE ###
  pass


# In[7]:


print(end_times) # End times for each process
print(wait_times) # Wait times for each process in the queue


# In[ ]:




