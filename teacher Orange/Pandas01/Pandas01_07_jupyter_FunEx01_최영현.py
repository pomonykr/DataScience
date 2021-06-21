#!/usr/bin/env python
# coding: utf-8

# # 매개변수 지정하여 호출하기
# ### 1. 일반적인 함수

# In[1]:


def add(a, b):	# a, b는 매개변수
	return a,b, a+b

a, b, result = add(b=5,a=3)
print("%d + %d = %d " % (b,a,result))
print("-"*20)


# ### 2. 입력값이 없는 함수

# In[2]:


def say():
	return 'Hi'

print(say())
print("-"*20)


# ### 3. 결괏값이 없는 함수
# #### 결괏값은 오직 return 명령어로만 돌려받을 수 있다.

# In[3]:


def add2(a, b):
	print("%d + %d = %d" %(a, b, a+b))

print(add2(3, 4))
print("-"*20)


# ### 4. 입력값도 결괏값도 없는 함수

# In[4]:


def say2():
	print('Hi')

say2()
print("-"*20)

