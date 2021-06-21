
# coding: utf-8

# In[2]:


import pandas as pd

#read_json() 함수로 데이터프레임 변환
df = pd.read_json('./DataSet/read_json_sample.json')
print(df,'\n')

print(df.index)

