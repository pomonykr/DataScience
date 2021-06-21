
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ["A","A+","B"],
       'basic' : ["C","B","B+"],
       'c++' : ["B+","C","C+"]}

df = pd.DataFrame(data)
df.set_index('name',inplace = True)
print(df)

#to_csv() 메소드를 사용하여 CSV 파일로 내보내기, 파일명은 df_sample.csv로 저장
df.to_json("./df_sample.json")


# In[3]:


data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ["A","A+","B"],
       'basic' : ["C","B","B+"],
       'c++' : ["B+","C","C+"]}

df = pd.DataFrame(data)
df.set_index('name',inplace = True)
print(df)

#to_csv() 메소드를 사용하여 CSV 파일로 내보내기, 파일명은 df_sample.csv로 저장
df.to_excel("./df_sample.xlsx")


# In[5]:


data1 = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ["A","A+","B"],
       'basic' : ["C","B","B+"],
       'c++' : ["B+","C","C+"]}

data2 = {'c0':[1,2,3],
        'c1' : [4,5,6],
        'c2' : [7,8,9],
        'c3' : [10,11,12],
        'c4' : [13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index('name',inplace = True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0',inplace = True)
print(df2)
#to_csv() 메소드를 사용하여 CSV 파일로 내보내기, 파일명은 df_sample.csv로 저장
writer = pd.ExcelWriter("./df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name = "시트1")
df2.to_excel(writer, sheet_name = "시트2")
writer.save()

