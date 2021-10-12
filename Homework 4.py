#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
import numpy as np
numbers = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
numbers * 2


# In[2]:


#Return Dimension
numbers.ndim


# In[3]:


#Return Shape
numbers.shape


# In[4]:


#Question 2
for row in numbers:
    for column in row:
        print(column, end = ' ')
    print()


# In[6]:


#Using flat method
for i in numbers.flat:
    print(i, end = ' ')


# In[7]:


#Question 3
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1,6])
ypoints = np.array([5,10])
plt.plot(xpoints, ypoints)
plt.show()


# In[8]:


#Question 4
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([3,6,9,12])
ypoints = np.array([2,8,1,10])
plt.plot(xpoints, ypoints, marker = 'D')
plt.show()


# In[9]:


#Question 5
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([2,4,6,14,10,12])
plt.plot(ypoints,'D--r', ms = 10, mec = 'g', mfc = 'g')
plt.show()


# In[ ]:




