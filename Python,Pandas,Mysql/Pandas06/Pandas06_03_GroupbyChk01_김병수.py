
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('./data/gapminder.tsv',sep='\t')


# In[4]:


type(df)


# In[8]:


type(df['pop'])


# In[9]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df['pop'])

