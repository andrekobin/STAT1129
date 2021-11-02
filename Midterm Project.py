#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import matplotlib.pyplot as plt

# Find the frequency of each distinct element in the list using a dictionary.
ulist = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
frequency = {}
for values in ulist:
    frequency[values] = ulist.count(values)
for key, values in frequency.items():
    print(key, ':', values)
    
# Plot the frequency results
plt.hist(ulist)

plt.xlabel("Number")
plt.ylabel("Frequency")

plt.title("Histogram: Frequency of Numbers in an Unsorted List")

plt.show()

# Store dictionary into file
with open('dictionaryresults.json', 'w') as file:
    json.dump(frequency, file, sort_keys=True, indent=1)


# In[2]:


import pandas as pd

# Read json file
df = pd.read_json('/Users/andrekobin/Desktop/your_posts_1.json')

df.head(3)


# In[5]:


import pandas as pd

#Reformatting Data to be Usable

#Read json file in DataFrame
df = pd.read_json('/Users/andrekobin/Desktop/your_posts_1.json')

#Renaming "timestamp" to "date"
df.rename(columns = {'timestamp': 'date'}, inplace = True)

#Removing Unnecessary Columns
df = df.drop(['attachments', 'title', 'tags'], axis = 1)

#Formatting to Correct "datetime"
pd.to_datetime(df['date'])

df.head(3)

print(df.shape)
df.tail(3)   

# Checking End of Data


# In[6]:


df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
post_counts


# In[7]:


# Visualizing Results
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Setting Figure Size and Font Size
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale = 5)

#Setting X Labels
x_labels = post_counts.index

#Creating Bar Plot
sns.barplot(x_labels, post_counts, color = "cyan")

#Showing x-axis labels for every year
tick_positions = np.arange(len(x_labels), step = 12)

#Reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

plt.show()


# In[ ]:




