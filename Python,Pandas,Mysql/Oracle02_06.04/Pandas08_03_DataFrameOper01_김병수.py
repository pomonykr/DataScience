
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns

#titanic 데이터셋에서 age,fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
print(titanic.columns,'\n',titanic.shape)
df = titanic.loc[:,['age','fare']]
print(df.head(),'\n')
print(type(df),'\n')

#데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head(),'\n')
print(type(addition))


# In[3]:


import pandas as pd
import seaborn as sns

#titanic 데이터셋에서 age,fare 2개 열을 선택하여 데에터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.tail(),'\n')
print(type(df),'\n',df.shape)

#데이터프레임에 숫자 10 더하기
addtion= df+10
print(addition.tail(),'\n')
print(type(addition),'\n')

#데이터프레임끼리 연산하기 (addition-df)
subtraction = addtion -df
print(subtraction.tail(),'\n')
print(type(subtraction))

