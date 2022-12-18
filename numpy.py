#!/usr/bin/env python
# coding: utf-8

# # My first file for numpy

# In[1]:


import numpy as np


# Numpy is library written in c thats why is faster than array, list, any other python objects

# In[2]:


myarr = np.array([3,4,64,32,34],np.int8)
myarr


# In[3]:


myarr[3]


# In[4]:


myarr = np.array([[2,3],[3,5]])
myarr.shape


# In[5]:


myarr.dtype


# In[6]:


myarr[0,1]  #numpy arrary are mutable i.e they can be changed


# In[7]:


myarr


# **There are 5 general mechanism for creating arrays:**
# 1. Conversion from other Python strictures(e.g list,tuple)
# 2. Intrinsic numpy creation objects (eg arange, ones, zeros, etc) 
# 3. Reading arrays from disk,either from standard or custum formats
# 4. Creating arrays from raw bytes through the use of strings or buffers
# 5. Use of special library functions(eg random)

# # Array creation: Conversion from other python stuctures

# In[8]:


myarr.size


# In[9]:


zeros = np.zeros((2,4))
zeros


# In[10]:


rng = np.arange(14)
rng


# In[11]:


lspace = np.linspace(0,20,5)
lspace


# In[12]:


emp = np.empty((4,3))
emp


# In[13]:


emplike = np.empty_like(lspace)
emplike


# In[14]:


ide = np.identity((45))
ide


# In[17]:


arr = np.arange(100)


# In[19]:


arr = arr.reshape(4,25)
arr


# In[20]:


arr = arr.ravel()
arr


# In[36]:


ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
ar


# In[27]:


A1 = ar.sum(axis = 0)
A2 = ar.sum(axis = 1)
A1, A2


# In[28]:


ar.nbytes # Total bytes consumed


# In[29]:


ar.T


# In[30]:


ar.flat
for item in ar.flat:
    print(item)


# In[31]:


ar.ndim


# In[32]:


ar.argmax() # place of max element


# In[33]:


ar.argsort() #sorts array


# In[39]:


np.where(ar>7)


# In[35]:


type(np.where(ar>5))


# In[41]:


np.count_nonzero(ar) # shows no of non zero elements in array


# In[44]:


np.nonzero(ar) #shos position of nonzero elements in array

