
# coding: utf-8

# In[5]:


import pandas as pd

# HTML 파일경로 or 웹 페이지 주소를 url 변수에 저장
url = './DataSet/Pandas04_08_Test01_김병수.html'
# HTML 웹페이지의 표를 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

# 표(table)의 개수 확인
print(len(tables),'\n==>')

print(tables,"\n==>")

#tables 리스트의 원소를 teration 하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]"%i,'\n')
    print(tables[i],'\n')
#파이썬 패키지 정보가 들어 있는 두 두번째 데이터프레임을 선택하여 df 변수에 저장
df = tables[1]
print(df.columns,"\n")

