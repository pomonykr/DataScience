
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('./data/scientists.csv')


# In[3]:


ages = scientists['Age']

print(ages.max())


# In[4]:


print(ages + ages)


# In[5]:


print(ages * ages)


# In[6]:


print(ages + 100)


# In[7]:


print(ages *2)


# In[8]:


print(pd.Series([1,100]))


# In[9]:


print(ages,'\n\n')
print(pd.Series([1,100]),'\n\n')
print(ages+pd.Series([1,100]))


# In[10]:


print(ages)


# In[11]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[12]:


print(ages *2)


# In[13]:


print(ages+rev_ages)

