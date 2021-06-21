
# coding: utf-8

# In[9]:


import pandas as pd


# In[18]:


df = pd.DataFrame({'Animal':['Falcon','Falcon',
                             'Parrot','Parrot'],
                  'Max Speed':[380.,370.,24.,26.]})
df


# In[19]:


df.groupby(['Animal']).mean()

