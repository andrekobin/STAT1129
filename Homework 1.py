#!/usr/bin/env python
# coding: utf-8

# In[ ]:


colors = ["blue", "teal", "black", "green"]
print(type(colors))
print(colors)


# In[3]:


nums = (list(range(30, 63, 3)))
print(type(nums))
print(nums)


# In[4]:


nums = ("30","33","36","39","42","45","48","51","54","57","60")
print(type(nums))
print(nums)


# In[16]:


nums = []
print(type(nums))
print(nums)
nums.append("0")
nums.append("1")
nums.append("2")
nums.append("3")
nums.append("4")
nums.append("5")
print(nums)
nums.remove("2")
print(nums)
nums.insert(2, "2.0")
print(nums)
print(len(nums))
print(max(nums))
print(min(nums))


# In[42]:


nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
total = sum(nums)
print(total)


# In[ ]:




