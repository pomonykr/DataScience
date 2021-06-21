
# coding: utf-8

# In[8]:


import pandas as pd
# red_csv_sample.csv
# pd.read_csv
file_path = "./DataSet/read_csv_sample.csv"
df = pd.read_csv(file_path)
print(df)
print(type(df))
df2 = pd.read_csv(file_path,header=None)
print(df2,'\n')
df3 = pd.read_csv(file_path,index_col=None)
print(df3,'\n')
df4 = pd.read_csv(file_path,index_col='c3')
print(df4,'\n')

