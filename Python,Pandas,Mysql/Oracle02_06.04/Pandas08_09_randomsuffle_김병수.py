
# coding: utf-8

# In[1]:


import random


# In[4]:


import pandas as pd


# In[5]:


scientists = pd.read_csv('./data/scientists.csv')


# In[6]:


ages = scientists['Age']

print(ages.max())


# In[11]:


random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])


# In[12]:


print(scientists['Age'])


# In[ ]:


print(scientists['Age'])

