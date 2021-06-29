
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('./data/scientists.csv')


# In[3]:


ages = scientists['Age']

print(ages.max())


# In[4]:


print(ages.mean())


# In[5]:


print(ages[ages > ages.mean()])


# In[6]:


print(ages > ages.mean())


# In[7]:


print(type(ages>ages.mean()))


# In[8]:


manual_bool_values = [True,True,False,False,True,True,False,True]
print(ages[manual_bool_values])

