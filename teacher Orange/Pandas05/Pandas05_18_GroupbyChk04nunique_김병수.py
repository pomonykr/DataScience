
# coding: utf-8

# In[18]:


import pandas as pd


# In[54]:


df = pd.read_csv('./data/gapminder.tsv',sep='\t')
df


# In[42]:


print(df.head(n=3))


# In[43]:


print(df.groupby('year')['lifeExp'].mean())


# In[48]:


for idx in uniList:
    print(idx,"=====> 1 :")
    grYear = df[df['year']==idx]
    print(len(grYear),"\n======> 2 \n:",grYear.head(3),"\n=====>3:",grYear.shape)
    print(grYear["lifeExp"].mean())


# In[44]:


df['year'].unique()


# In[64]:


print(df.groupby('continent')['year'].count())


# In[58]:


ConList = df['continent'].unique()
print(ConList)


# In[62]:


for idx in ConList:
    print(idx,"=====> 1 :")
    grCon = df[df['continent']==idx]
    print(len(grCon),"\n======> 2 \n:",grCon.head(3),"\n=====>3:",grCon.shape)
    print(grCon['continent'].count())


# In[65]:


print(df.groupby('continent')['year'].nunique(),"\n====>")
print(df.groupby('continent')['year'].unique(),"\n====>")
print(df.groupby('continent')['year'].unique()['Africa'],"\n====>")

