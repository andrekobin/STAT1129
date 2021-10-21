#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Question 1
import matplotlib.pyplot as plt
import numpy as np
y1 = np.array([1,2,3,4,5])
y2 = np.array([5,6,7,8,9])
y3 = np.array([9,10,11,12,13])
plt.plot(y1, linewidth = '2')
plt.plot(y2, linewidth = '2')
plt.plot(y3, linewidth = '2')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


# In[2]:


#Question 2
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(0,0.2,800)
plt.hist(x)
plt.show()


# In[4]:


#Question 3
mydic = {"Apples":45, "Bananas":25, "Cherries":15, "Dates":20}
fruit_list = list(mydic.keys())
count_list = list(mydic.values())
print(fruit_list)
print(count_list)

import matplotlib.pyplot as plt
import numpy as np
y = np.array(count_list)
mylabels = fruit_list
myexplode = [0.1, 0.1, 0.1, 0.1]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.legend()
plt.show()

x = np.array(fruit_list)
y = np.array(count_list)
plt.bar(x, y, width = 0.8)
plt.show()


# In[5]:


#Question 4
import matplotlib.pyplot as plt
import numpy as np
art_marks = [88,92,80,89,90,80,60,88,80,84]
marks_range = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(marks_range, art_marks, color = 'r')

science_marks = [75,59,69,48,65,56,32,45,20,30]
marks_range = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(marks_range, science_marks, color = 'g')

plt.legend(['Art Marks', 'Science Marks'])
plt.title("Scatter Plot")
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")

plt.show()


# In[14]:


#Question 5
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([14,2,5,11,5])
y2 = np.array([4,9,2,5,11])
plt.subplot(1,4,1)
plt.plot(y1)
plt.plot(y2)
plt.title("Multiple Line Plot")

x = np.array([4,1,10,15,4,21,7])
y = np.array([13,56,34,75,124,32,12])
plt.subplot(1,4,2)
plt.scatter(x,y)
plt.title("Scatter Plot")

x = np.array(["Tall", "Short"])
y = np.array([92,43])
plt.subplot(1,4,3)
plt.bar(x,y)
plt.title("Bar Chart")

x = np.random.normal(0,0.6,1200)
plt.subplot(1,4,4)
plt.hist(x)
plt.title("Histogram")

plt.show()


# In[ ]:




