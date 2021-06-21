
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('./data/scientists.csv')


# In[3]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)


# In[5]:


born_datetime = pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
print(born_datetime)


# In[6]:


died_datetime = pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
print(died_datetime)


# In[7]:


died_datetime2 = died_datetime - born_datetime


# In[8]:


print(died_datetime2)


# In[9]:


scientists['born_dt'],scientists['died_dt']=(born_datetime,died_datetime)
print(scientists.head())


# In[10]:


print(scientists.shape)


# In[11]:


scientists['age_days_dt'] = (scientists['died_dt']-                            scientists['born_dt'])
print(scientists)

