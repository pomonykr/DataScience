
# coding: utf-8

# In[4]:


import pandas as pd
# red_csv_sample.csv
# pd.read_csv
file_path = "./DataSet/read_csv_sample.csv"
df = pd.read_csv(file_path)
print(df)
print(type(df))

