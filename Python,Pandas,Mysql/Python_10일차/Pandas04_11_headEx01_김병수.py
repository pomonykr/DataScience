
# coding: utf-8

# In[16]:


import pandas as pd


# In[15]:


df = pandas.read_csv('./data/gapminder.tsv',sep='\t')

print(df)


# In[17]:


df= pd.DataFrame({'animal':['alligator','bee','falcon','lion','monkey','parrot','shark','whale','zebra']})


# In[18]:


print(df)


# In[19]:


print(df.head())


# In[20]:


print(df.head(-3))

