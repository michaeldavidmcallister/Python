#!/usr/bin/env python
# coding: utf-8

# ## CIND830 - Python Programming for Data Science  
# ### Assignment 1 (10% of the final grade) 
# ### Due on May 17, 2021 11:59 PM  

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
# 

# ### Question 1  **[30 pts]**:
# 
# **a)**  **[10 pts]**  Write a Python program that accepts a list of marks then prints the letter grade and description according to the [Grading System](https://continuing.ryerson.ca/contentManagement.do?method=load&code=CM000034) of the Chang School of Continuing Education.
# 
# For example, if the user enters `90, 120, -12, 71.5, 62.5`, the output would be as follows:
# 
# | Mark | Letter Grade | Performance Description |
# |:-:|:-:|:-:|
# | 90 | A+ | Excellent |
# | 120 | Not Possible | Not Possible |
# | -12 | Not Possible | Not Possible |
# | 71.5 | B- | Good |
# | 62.5 | C | Satisfactory |

# In[1]:


'''Grading System:  
Excellent	
A+	90-100	4.33
A	85-89	4.00
A-	80-84	3.67
Good	
B+	77-79	3.33
B	73-76	3.00
B-	70-72	2.67
Satisfactory	
C+	67-69	2.33
C	63-66	2.00
C-	60-62	1.67
Marginal	
D+	57-59	1.33
D	53-56	1.00
D-	50-52	0.67
Unsatisfactory	
F	0-49	0'''

#Accept comma separated list and assign the values
numericGrades = list(input("Please enter grades to be evaluated: ").split(", "))
print("Mark     Letter Grade     Performance Description")
numericGrades = [float(i) for i in numericGrades]
for i in numericGrades:
    if i >100:
        print(i, "\t", 'Not Possible', "\t", "Not Possible")
    elif i >=90:
        print(i,"\t",'A+',"\t",'Excellent')
    elif i >= 85:
        print(i,"\t",'A',"\t",'Excellent')
    elif i >= 80:
        print(i,"\t",'A-',"\t",'Excellent')
    elif i >= 77:
        print(i,"\t",'B+',"\t",'Good')
    elif i >= 73:
        print(i,"\t",'B',"\t",'Good')
    elif i >= 70:
        print(i,"\t",'B-',"\t",'Good')
    elif i >= 67:
        print(i,"\t",'C+',"\t",'Satisfactory')
    elif i >= 63:
        print(i,"\t",'C',"\t",'Satisfactory')
    elif i >= 60:
        print(i,"\t",'C-',"\t",'Satisfactory')
    elif i >= 57:
        print(i,"\t",'D+',"\t",'Marginal')
    elif i >= 53:
        print(i,"\t",'D',"\t",'Marginal')
    elif i >= 50:
        print(i,"\t",'D-',"\t",'Marginal')
    elif i >= 0:
        print(i, "\t",'Unsatisfactory', "\t", 'Unsatisfactory')
    else:
        print(i, "\t",'Not Possible', "\t", 'Not Possible')


# **b)**  **[10 pts]** Write a code to compute and print the sum of squares of only the `Excellent` marks.
# 
# For example, if the user enters `90.5, 120, -12, 71.3, 82.2, 62.5`, then the output should be: <br>
# `The Excellent marks are:  [90.5, 82.2]`<br>
# `The sum of squares is  14947.09`

# In[47]:


get_ipython().run_line_magic('reset', '-f')
#resetting variables to avoid residue from prior runs
ExcellentMarks = []
Square = []
#defining my variables as lists

newGrades = list(input("Please enter grades to be evaluated: ").split(", "))
newGrades = [float(i) for i in newGrades]
for i in newGrades:
    if i >= 80 and i <= 100:
        ExcellentMarks.append(i)
        Square.append(i*i)
#iterating the input and creating two lists; ExcellentMarks and Square, modifying Square to give square value

SumSquare = sum(Square)
print('The Excellent Marks are: ', ExcellentMarks)
print('The Sum of Squares are: ', SumSquare)


# **c)**  **[10 pts]** Write a code to compute and print the `Median`, `Average` and `Mode` of the marks between 0 and 100 after rounding each mark to the nearest integer.  Ensure notifying the user if there is no unique mode found, as the `Mode` in this exercise returns only the single most common mark in the list.
# 
# For example, if the user enters `89.7, 120, -12, 90, 60.2`, then the output should be: <br>
# `The valid marks are:  [90, 90, 60] `<br>
# `Median is 90 ; Average is 80 ; Mode is 90`
# 
# However, if the user enters `90.6, 70, 100, 40.4`, then the output should be: <br>
# `The valid marks are:  [91, 70, 100, 40] `<br>
# `Median is 80.5 ; Average is 75.25 ; No unique mode found`
# 
# Also, if the user enters `65, 65, 65, 35, 35, 35`, then the output should be: <br>
# `The valid marks are:  [65, 65, 65, 35, 35, 35] `<br>
# `Median is 50.0 ; Average is 50 ; No unique mode found`
# 
# **Hint:** Use the `statistics` module as it provides functions to calculate mathematical statistics of numeric data.

# In[115]:


get_ipython().run_line_magic('reset', '-f')
#cleared all variables to avoid residue from prior values in variables, plus imported the statistics module

from statistics import mean, median, mode

validMarks = []

numericGrades = list(input("Please enter grades to be evaluated: ").split(", "))
numericGrades = [float(i) for i in numericGrades]
for i in numericGrades:
    if i >= 0 and i <= 100:
        validMarks.append(i)
for i in range(0, len(validMarks)):
    validMarks[i] = round(validMarks[i])
print('The valid Marks are: ', (validMarks))
try:
    print(' Median is ', median(validMarks) , '; ', 'Average is ', mean(validMarks), '; ', 'The mode is: ', mode(validMarks))
except:
    print(' Median is ', median(validMarks) , '; ', 'Average is ', float(mean(validMarks)), '; ','No Unique Mode Found')


# *****

# 
# ### Question 2  **[40 pts]**:
# **a)**  **[10 pts]** Write a code that creates a set of different passwords.  Each password is a combination of a random adjective, noun, two digits and two punctuation symbols.
# 
# For example, if the user asks for generating 4 passwords, then the code might generate the following list:
# 
# | Password |
# |:-|
# | supershine17*-  |
# | cheerfulmeet78~.  |
# | elitemango32&,  |
# | glossytrain14$} |
# 
# **Hint:**  You can use the `wonderwords` library to generate random words of the English language

# In[200]:


get_ipython().run_line_magic('reset', '-f')
from wonderwords import RandomWord
import random
import string
n=int(input("Enter n:"))
#Create an empty list
passwordlist=[]

print("Password")  
for i in range(1,n+1):
    r= RandomWord()
    adjectives=r.word(include_parts_of_speech=["adjectives"])
    nouns=r.word(include_parts_of_speech=["nouns"])
    #Generate 2 random digits
    digit=random.randint(0,9)
    digit2=random.randint(0,9)
    #convert the integers to strings so it can be concatenated
    digit=str(digit)
    digit2=str(digit2)
    #Create 2 random characteres
    symbol1=random.choice(string.punctuation)
    symbol2=random.choice(string.punctuation)
    #concatenate all variables to get the password
    password=adjectives+nouns+digit+digit2+symbol1+symbol2
    print(password)


# **b)**  **[10 pts]** Count the letters of each generated password in Q2.a, then print the password along with its number of letters.
# 
# For example, if the user enters 4, then the output might be as follows:
# 
# | Password | Length |
# |:-|:-|
# | supershine17*-  | 14 |
# | cheerfulmeet78~.  | 16|
# | elitemango32&,  | 14|
# | glossytrain14$} | 15 |
# 
# 

# In[179]:


get_ipython().run_line_magic('reset', '-f')
from wonderwords import RandomWord
import random
import string
n=int(input("Enter n:"))
#Create an empty list
passwordlist=[]

for i in range(1,n+1):
    r= RandomWord()
    adjectives=r.word(include_parts_of_speech=["adjectives"])
    nouns=r.word(include_parts_of_speech=["nouns"])
    #Generate 2 random digits
    digit=random.randint(0,9)
    digit2=random.randint(0,9)
    #convert the integers to strings so it can be concatenated
    digit=str(digit)
    digit2=str(digit2)
    #Create 2 random characteres
    symbol1=random.choice(string.punctuation)
    symbol2=random.choice(string.punctuation)
    #concatenate all variables to get the password
    password=adjectives+nouns+digit+digit2+symbol1+symbol2
    #putting the password in a list
    passwordlist.append((password,len(password)))
#printing the password
print("Password\t\t\tLength")   
for i in range(len(passwordlist)):
    print(passwordlist[i][0],"\t\t",passwordlist[i][1])


# **c)**  **[10 pts]** Write a code to print only the passwords with more than 14 letters and either the letter 'o', the digit '3', or the punctuation symbol '~'.
# 
# For example, the code would filter the 4 passwords listed in 2.a, and print the following output:
# 
# | Password | Length |
# |:-|:-|
# | cheerfulmeet78~.  | 16|
# | glossytrain14$} | 15 |

# In[115]:


get_ipython().run_line_magic('reset', '-f')
from wonderwords import RandomWord
import random
import string

n=int(input("Enter n:"))
#Create an empty list
passwordlist=[]

for i in range(1,n+1):
    r= RandomWord()
    adjectives=r.word(include_parts_of_speech=["adjectives"])
    nouns=r.word(include_parts_of_speech=["nouns"])
    #Generate 2 random digits
    digit=random.randint(0,9)
    digit2=random.randint(0,9)
    #convert the integers to strings so it can be concatenated
    digit=str(digit)
    digit2=str(digit2)
    #Create 2 random characteres
    symbol1=random.choice(string.punctuation)
    symbol2=random.choice(string.punctuation)
    #concatenate all variables to get the password
    password=adjectives+nouns+digit+digit2+symbol1+symbol2
    #adding condition to adding password to the passwordlist list
    if len(password) >14 and "o" in password or "3" in password or "'" in password:
        passwordlist.append((password,len(password)))   
    else:
        pass
print("Password\t\t\tLength")
for i in range(len(passwordlist)):
    print(passwordlist[i][0],"\t\t",passwordlist[i][1])


# **d)**  **[10 pts]** Design an encoder that encrypts the passwords generated in Q2.a. by changing their letters into the octal form.
# 
# For example, if the user enters 4, then the output might be as follows
# 
# | Password | Encryption |
# |:-|:-|
# | supershine17*- | 0o1630o1650o1600o1450o1620o1630o1500o1510o1560o1450o610o670o520o55 |
# | cheerfulmeet78~. | 0o1430o1500o1450o1450o1620o1460o1650o1540o1550o1450o1450o1640o670o700o1760o56 |
# | elitemango32&, | 0o1450o1540o1510o1640o1450o1550o1410o1560o1470o1570o630o620o460o54 |
# | glossytrain14$} | 0o1470o1540o1570o1630o1630o1710o1640o1620o1410o1510o1560o610o640o440o175 |

# In[23]:


#%reset -f
#pip install wonderwords
from wonderwords import RandomWord
import random
import string
n=int(input("Enter n:"))
#Create an empty list
print("Password")
for i in range(1,n+1):
    r= RandomWord()
    adjectives=r.word(include_parts_of_speech=["adjectives"])
    for i in range(1,n+1):
        oct(ord(i)) in adjectives
        adjoct += i
    nouns=r.word(include_parts_of_speech=["nouns"])
    for i in range(1,n+1):
        oct(ord(i)) in nouns
        nounoct += i
    #Generate 2 random digits
    digit1=random.randint(0,9)
    digoct1 += oct(digit1)
    digit2=random.randint(0,9)
    digoct2 += oct(digit2)
    #Create 2 random characteres
    symbol1=random.choice(string.punctuation)
    symoct1 += oct(ord(symbol1))
    symbol2=random.choice(string.punctuation)
    symboct2 += oct(ord(symbol2))
    password = adjoct + nounoct + digoct1 + digoct2 + symoct1 + symoct2
print(password)


# *****

# ### Question 3  **[30 pts]**:
# 
# Write a program that accepts the coefficients of the following two lines as inputs
# 
# Line1: $a_1x+b_1y + c_1 = 0$
# 
# Line2: $a_2x+b_2y + c_2 = 0$
# 
# Then checks whether the two lines are parallel, intersecting or overlapping according to the conditions listed below.

# **a)**  **[10 pts]** Intersecting lines: If $\frac{a_1}{a_2} \ne \frac{b_1}{b_2}$

# In[27]:


#Promp user for coefficients of line 1
print("Line : a1x + b1y + c1 = 0")
print("Enter coefficient for line 1")
a1 = int(input("a1 : "))
b1 = int(input("b1 : "))
c1 = int(input("c1 : "))

#Promp user for coefficients of Line 2
print("Line : a2x + b2y + c2 = 0")
print("Enter coefficient for line 2")
a2 = int(input("a2 : "))
b2 = int(input("b2 : "))
c2 = int(input("c2 : "))

if (a1/a2 != b1/b2):
    print("The Lines are Intersecting")
elif (a1/a2 == b1/b2 != c1/c2):
    print("The lines are parallel")
elif (a1/a2 == b1/b2 == c1/c2):
    print("The lines overlap")


# **b)**   **[10 pts]** Parallel lines: If the lines are not intersecting and $\frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2}$

# In[29]:


#Promp user for coefficients of line 1
print("Line : a1x + b1y + c1 = 0")
print("Enter coefficient for line 1")
a1 = int(input("a1 : "))
b1 = int(input("b1 : "))
c1 = int(input("c1 : "))

#Promp user for coefficients of Line 2
print("Line : a2x + b2y + c2 = 0")
print("Enter coefficient for line 2")
a2 = int(input("a2 : "))
b2 = int(input("b2 : "))
c2 = int(input("c2 : "))

if (a1/a2 != b1/b2):
    print("The Lines are Intersecting")
elif (a1/a2 == b1/b2 != c1/c2):
    print("The lines are parallel")
elif (a1/a2 == b1/b2 == c1/c2):
    print("The lines overlap")


# **c)**   **[10 pts]** Overlapping lines: If the lines are not intersecting and $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$

# In[31]:


#Promp user for coefficients of line 1
print("Line : a1x + b1y + c1 = 0")
print("Enter coefficient for line 1")
a1 = int(input("a1 : "))
b1 = int(input("b1 : "))
c1 = int(input("c1 : "))

#Promp user for coefficients of Line 2
print("Line : a2x + b2y + c2 = 0")
print("Enter coefficient for line 2")
a2 = int(input("a2 : "))
b2 = int(input("b2 : "))
c2 = int(input("c2 : "))

if (a1/a2 != b1/b2):
    print("The Lines are Intersecting")
elif (a1/a2 == b1/b2 != c1/c2):
    print("The lines are parallel")
elif (a1/a2 == b1/b2 == c1/c2):
    print("The lines overlap")


# **BONUS**   **[10 pts]** Plot the two lines graphically using the `matplotlib` and `numpy` libraries or any other suitable libraries. 

# In[87]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Promp user for coefficients of line 1
print("Line : a1x + b1y + c1 = 0")
print("Enter coefficients for line 1")
a1 = int(input("a1 : "))
b1 = int(input("b1 : "))
c1 = int(input("c1 : "))

#Promp user for coefficients of Line 2
print("Line : a2x + b2y + c2 = 0")
print("Enter coefficients for line 2")
a2 = int(input("a2 : "))
b2 = int(input("b2 : "))
c2 = int(input("c2 : "))

a = [a1,b1,c1]
b = [a1,b2,c2]

plt.plot(a, color='grey')
plt.plot(b, color='red')
plt.title("A in Grey, B in Red")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[4]:


pip install wonderwords


# In[3]:


get_ipython().system(' jupyter nbconvert --assignment 1.ipynb')


# *****
# 
# 

# #### This is the end of assignment 1
