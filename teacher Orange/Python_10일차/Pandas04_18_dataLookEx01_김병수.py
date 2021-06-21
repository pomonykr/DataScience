
# coding: utf-8

# In[16]:


import pandas as pd


# In[28]:


df = pd.read_csv('./data/gapminder.tsv',sep='\t')
print(df)
df.shape


# In[29]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[36]:


len(df)


# In[35]:


df.head()


# In[34]:


df[0:5]


# In[33]:


df.head(n=7)


# In[32]:


df.tail()


# In[31]:


df[len(df)-5:len(df)+1]


# In[30]:


df.tail(n=7)


# In[37]:


type(df)


# In[38]:


print(df.columns)


# In[39]:


df.index


# In[40]:


print(df.dtypes)


# In[41]:


print(df.info())


# In[42]:


df.shape

