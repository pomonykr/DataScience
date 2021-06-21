
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('./data/scientists.csv')


# In[3]:


print(scientists[scientists['Age']>scientists['Age'].mean()])


# In[4]:


print(scientists.loc[[True,True,False,True]])


# In[5]:


print(scientists * 2)

