
# coding: utf-8

# In[1]:


#라이브러리 불러오기
import pandas as pd
import numpy as np


# In[2]:


student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행(시리즈vs시리즈)
addition = student1+ student2
subtraction = student1 - student2
multiplication = student1 * student2
division       = student1 / student2
print(type(division),'\n')

#사칙연산 결과를 데이터프레임으로 합치지(시리즈->데이터프레임)
result = pd.DataFrame([addition,subtraction,multiplication,division],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result,'\n')


# In[4]:


student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행 (연산메소드 사용)
sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈->데이터프레임)
result = pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

