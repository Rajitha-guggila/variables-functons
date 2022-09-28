#!/usr/bin/env python
# coding: utf-8

# In[1]:


#GLOBAL VARIABLES

greeting ="good morning"
def greet_kevin():
    name1="kevin"
    print(greeting,name1)

def greet_enow():
    name2="enow"
    print(greeting,name2)

def greet_rajitha():
    name3="rajitha"
    print(greeting,name3)


greet_kevin()
greet_enow()
greet_rajitha()


# In[3]:


#LOCAL VARIABLES

global name2
greeting="website name is"
name="Software testing"
name2="software developer"
print(greeting,name2)


# In[14]:


#built in functions

plant1="A Small plant in my house"
plant2="A Small plant2 in my house"

def myroom():
    myplant ="money plant in myroom"
    
print("i have",plant1)
print(plant2)


# In[15]:


def my_function(x):
    out=5*x
    return out
print(my_function(3))
print(my_function(5))


# In[ ]:




