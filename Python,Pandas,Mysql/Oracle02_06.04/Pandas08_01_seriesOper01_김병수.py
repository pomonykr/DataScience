
# coding: utf-8

# In[ ]:


#라이브러리 불러오기
import pandas as pd


# In[5]:


#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90 })
print(student1,'\n')

#학생의 과목별 점수를 200으로 나누기
percentage = student1 /200

print(percentage,'\n')
print(type(percentage))


# In[3]:


#라이브러리 불러오기
import pandas as pd

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90,'영어':80})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행
addition = student1+ student2
subtraction = student1 - student2
multiplication = student1 * student2
division       = student1 / student2
print(type(division),'\n')

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈->데이터프레임)
result = pd.DataFrame([addition,subtraction,multiplication,division],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result,'\n',type(sesult))
print(addition,'\n',subtraction,'\n',multiplication,'\n',divition)

