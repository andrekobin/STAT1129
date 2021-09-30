#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = {'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
for name,grade in marks.items():
    print(name,grade)


# In[3]:


grade_sum = sum(marks.values())
grade_count = list(marks.values())
grade_mean = grade_sum / len(grade_count)
print("The mean grade of the students is" , grade_mean)
grade_max = max(marks.values())
print("The maximum grade is", grade_max)
grade_min = min(marks.values())
print("The minimum grade is", grade_min)


# In[4]:


for name in marks.keys():
    if 'J' in name:
        break
    print(name)


# In[5]:


for name in marks.keys():
    if 'J' in name:
        continue
    print(name)


# In[8]:


#I searched for the name Andy and then my own name to test the else statement
def students(student_name):
    marks = {'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print("The students name has not been found")
students("Andy")
students("Andre")


# In[9]:


#I used the 4th power in this question
def less_than(num):
    n = 0
    while n < num:
        m = n**4
        print("When n is:",n,"The power of n is:",m)
        n += 1
    else:
        print("Greater than",num)
less_than(8)


# In[10]:


#I used integers 1 to 100 to test the function
def integers(num):
    n = 1
    total = 0
    while n <= num:
        total += n
        n += 1
    print("The sum is",total)
integers(100)


# In[11]:


def integers(num):
    total = 0
    for n in range(1,num + 1):
        total += n
        print("The sum is",total)
integers(10)


# In[12]:


def minimum(v1,v2,v3,v4):
    min_value = v4
    if v1 < min_value:
        min_value = v1
    if v2 < min_value:
        min_value = v2
    if v3 < min_value:
        min_value = v3
    return min_value
minimum(145,23,16,90)


# In[ ]:




