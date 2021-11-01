#!/usr/bin/env python
# coding: utf-8

# ## CIND830 - Python Programming for Data Science  
# ### Assignment 2 (10% of the final grade)
# ### Due on May 31, 2021 11:59 PM

# *****
# This is a Jupyter Notebook document that extends a simple formatting syntax for authoring HTML and PDF. Review [this](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) website for more details on using Jupyter Notebooks.
# 
# Use the JupyterHub server on the Google Cloud Platform, provided by your designated instructor, for this assignment. Ensure using **Python 3.7.6** release then complete the assignment by inserting your Python code wherever seeing the string `#INSERT YOUR ANSWER HERE.`
# 
# When you click the `File` button, from the top navigation bar, then select `Export Notebook to HTML`, an HTML document will be generated that includes both the assignment content and the output of any embedded Python code chunks.
# 
# Use [these](https://www.ryerson.ca/courses/students/tutorials/assignments/) guidelines to submit **both** the IPYNB and the exported file (HTML). Failing to submit both files will be subject to mark deduction.
# 
# Please be advised that you cannot get more than 100% in this assignment, and the **BONUS** question will only be graded if all other questions have been submitted.

# *****

# ### Question 1 **[50 pts]**:

# **a)** **[10 pts]** Define a function called `is_even` that takes an integer as a parameter and returns `True` if the given integer is Even. An integer is said to be even if the modulo(%) of the integer equals `0`. For example, `4` is even `(4%2 = 0)`, but `5` is not `(5%2 = 1)`.

# In[55]:


#Function = is_even
#Takes integer from input, returns true if even

def is_even(x):
    return x%2 == 0

is_even(2) # True
is_even(4) #True
is_even(3) #False


# **b)** **[10 pts]** Modify the `is_even` function you created in Q1.a to take a floating-point data as an input and return `True` if the ceiling of the input is Even. For example, `12.5` is not even, but `11.25` is even.

# In[7]:


import math

def is_Even(x):
    x = math.ceil(x)
    return x%2 == 0

is_even(12.5) #False
is_even(11.25) #True


# **c)** **[10 pts]** Define a function called `is_even_vec` that calls `isEven` function you updated in Q1.b to take a list of floating-point or integer numbers and return their results in a list.  For example, given `[1441.25, 231.5, 23]` the function returns `[True, True, False]`

# In[57]:


import math

def is_Even(x):
    x = math.ceil(x)
    return x%2 == 0


def is_even_vec(x):
    output=[]
    for i in x:
        z = is_Even(i)
        output.append(z)
    return(output)
        
is_even_vec([1441.25, 231.5, 23])


# d)**[10 pts]** Define a function called `is_even_dict` that calls `is_even_vec` and returns the results in a dictionary with their corresponding input elements. \
# For example, given `[1441.25, 231.5, 23]` the function returns `{1441.25: True, 231.5: True, 23: False}`

# In[93]:


#define the keys as the inputted list
#define the output of is_even_vec as the values of the dictionary



import math

def is_Even(x):
    x = math.ceil(x)
    return x%2 == 0


def is_even_vec(x):
    output=[]
    for i in x:
        z = is_Even(i)
        output.append(z)
    return(output)

def is_even_dict(x):
    dictionary={} #initialize dictionary
    #Storing starting values as keys
    #Storing is_even_vec values as values for dictionary
    key=x
    value=is_even_vec(x)
    #iterate through lists to match keys with values
    for i in key:
        for j in value:
            dictionary[i] = j
            value.remove(j)
            break
            return (dictionary)
#print dictionary
    print(dictionary)

is_even_dict([1441.25, 231.5, 23])



# **e)** **[10 pts]** Define a function called `isEvenTuple` by modifying the function you created in Q1.d to traverse the values of the returned dictionary **in reverse order** and return the dictionary keys that has a **`TRUE`** value as a tuple.  For example, given `[1441.25, 231.5, 23]` the function returns `(231.5 1441.25)`.

# In[108]:


import math

def is_Even(x):
    x = math.ceil(x)
    return x%2 == 0

def is_even_vec(x):
    output=[]
    for i in x:
        z = is_Even(i)
        output.append(z)
    return(output)

def isEvenTuple(x):
    list = []
    key=x
    value=is_even_vec(x)
    for i in key:
        for j in value:
            if j == True:
                list.insert(0,i)
                value.remove(j)
                break
    return(tuple(list))
    
isEvenTuple([1441.25, 231.5, 23])


# *****

# 
# 
# ### Question 2 **[30 pts]** :
# 
# 

# **a) **[10 pts]** Define a function called `three_sub_str` that takes in as input a string and returns a string made of the first 3 and the last 3 characters from the input. If the string length is less than 3, return instead the string `Not Possible`.
# 
# Examples:
# 1. Input: 'watermelon'; Output: 'watlon
# 2. Input: 'try'; Output: 'trytry'
# 3. Input: 'as'; Output: Not Possible

# In[46]:


def three_sub_str (x):
    if len(x) >2:
        y = x[0:3] + x[-3:]
    else:
        y = 'Not Possible'
    print("Input: \'" + x + "\'; Output: \'" + y + '\'')

three_sub_str('watermelon')
three_sub_str('try')
three_sub_str('as')
    


# **b)** **[10 pts]** Define a function `five_reverse` that takes as input a string and returns the reverse of the string if its length is a multiple of 5 else returns the original string.
# 
# Examples:
# 1. Input: 'GreenApple'; Output: 'elppAneerG'
# 2. Input 'RedApple'; Output 'RedApple'

# In[48]:


def five_reverse(x):
    if len(x) % 5 == 0:  
        y = x[::-1]
    else:
        y = x
    print("Input: \'" + x + "\'; Output: \'" + y + '\'')

five_reverse('GreenApple')
five_reverse('RedApple')


# **c)** **[10 pts]** Define a function `count_char` that takes in as input a string and a boolen value and returns a dictonary that has each charater in the string as key and the count of the number of times the character appeared in the string as value. If the boolean value is `True` then it returns the dict with only the most frequent character else returns the entire dictonary
# 
# Examples:
# 1. Input: 'apple', False; Output: {'a': 1, 'p': 2, 'l': '1', e: '1'}
# 2. Input: 'apple', True; Output: {'p': 2}

# In[116]:


def count_char(x, y):
    if y is True:
        highesta = 0
        output = {}
        for i in x:
            if x.count(i) > highesta:
                highesta = x.count(i)
                highestb = i
        output[highestb]=highesta
        print('Input: ', x,', TRUE; Output: ',output)
    elif y is False:
        output = {}
        for i in x:
            output[i]=x.count(i)
        print('Input: ', x, ', FALSE; Output: ',output)
            
count_char('apple', False)
count_char('apple', True)
    


# **BONUS** **[10 pts]** Define a function called `min_sub_str` that takes two string arguments ( S and T ) and returns the first possible substring (traversing from left) containing all the elements of `T`. For example: given `S = 'xBxxAxxCxxAxCxxBxxxAxCxBxxxAxxBxCx'` and `T = "ABC"`, returns **`"BxxAxxC"`**
# 

# In[52]:


#Look for A, B or C in any order from T
#returns the entire string from first character to the last in T

def min_sub_str(S, T):
    start_ind = [] 
    for i in range(len(S)):
        if S[i] in T:
             start_ind += [i]
    return S[start_ind[0]:start_ind[2]+1]

min_sub_str('xBxxAxxCxxAxCxxBxxxAxCxBxxxAxxBxCx', T= "ABC")


# *****

# ### Question 3 **[20 pts]**:
# 

# Define three classes, `Polygon`, `Rectangle` and `Square`. `Polygon` will be the parent class of `Triangle` and `Square`.
# 
# 1. The `Polygon` should have a function called `WhoAmI` and it should print out `Triangle` if the current object is a triangle or `Square` if the current object is a square.
# 
# 2. When you create a `Rectangle` object it should generate 2 random integers as the sides of the rectangle and store the values in the class.
# 
# 3. Similarly, for `Square` it should randomly generate 1 random integer to denote one side of the square and store it in the class. 
# 
# 4. Also, each of the `Rectangle` and `Square` classes should have a function called `findArea` that computes and returns the `Polygon` area. 
# 
# 5. The `Polygon` should have a function called `side_lengths` to print the side lengths of the polygon.
# 
# 6. The sides can be any value between 1 and 100, Inclusively.
# 
# Create 5 Triangle and 5 Square objects and print out all the properties in a loop.
# 
# It would be best if you mimicked this behaviour.
# 
# ```
# rect_obj = Rectangle()
# sq_obj = Square()
# 
# rect_obj.WhoAmI()
# Output "Rectangle"
# 
# rect_obj.side_lengths()
# Output: [5,6] // Random integers that were chosen
# 
# rect_obj.findArea()
# Output: 30
# 
# sq_obj.WhoAmI()
# Output: "Square"
# 
# sq_obj.side_lengths()
# Output: [6]
# 
# sq_obj.findArea()
# Output: 36
# ```

# In[58]:


import random

class Polygon:
        def __init__(self) :
                self.name = "Polygon"
                self.sides = []
                
        def whoAmI(self) :
                print("I am a", self.name)
                
        def side_lengths(self) :
                print("sides =", self.sides)
                
        def findArea(self):
                if(len(self.sides) > 2) :    # area of Triangle.
                        a, b = self.sides[0], self.sides[1]
                        c = ((a**2)+(b**2))**.5   #used pythagoran theorum to calculate C's value
                        p = (a + b + c) / 2
                        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
                        print("area =", round(area, 3))
                
                elif(len(self.sides) > 1) :  # area of Rectangle.
                        l, b = self.sides[0], self.sides[1]
                        print("area =", 2*(l + b))
                
                else:         # area of Square.
                        print("area =",self.sides[0] ** 2)

# Triangle inherits Polygon
class Triangle(Polygon):
        def __init__(self):
                self.name = "Triangle"
                self.sides = []
                m, n = random.uniform(2.0, 10.0), 1
                a = round(m * m - n * n, 2)             
                b = round(2 * m * n, 2)      # sum of any two sides should be greater than 3rd 
                c = round(m * m + n * n, 2)             
                self.sides.append(a)
                self.sides.append(b)    # add sides.
                self.sides.append(c)


# Rectangle inherits Polygon            
class Rectangle(Polygon):
        def __init__(self):
                self.name = "Rectangle"
                self.sides = []
                # generate side1 randomly 
                self.side = random.randint(1, 100)      
                self.sides.append(self.side)    
                # generate side2 randomly 
                self.side = random.randint(1, 100)      
                self.sides.append(self.side)
        
# Square inherits Rectangle
class Square(Rectangle):
        def __init__(self):
                self.name = "Square"
                self.sides = []
                # generate side randomly 
                self.side = random.randint(1, 100)
                self.sides.append(self.side)

def main():
        count = 1
        while(count <= 5):
                
                print(f"\n--- Triangle-{count}---")
                t1 = Triangle()
                t1.whoAmI()
                t1.side_lengths()
                t1.findArea()
                
                print(f"\n--- Square-{count}---")
                s1 = Square()
                s1.whoAmI()
                s1.side_lengths()
                s1.findArea()
                
                count+= 1

main()  # Create 5 Triangle and 5 Square objects and print out all the properties in a loop
print("\n")
    


# #### This is the end of assignment 2

# In[ ]:




