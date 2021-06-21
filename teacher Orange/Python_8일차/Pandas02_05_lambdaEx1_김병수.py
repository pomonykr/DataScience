#lambda
'''
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들 때 사용한다.
우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나
def를 사용할 수 없는 곳에 주로 쓰인다.

사용형식]
	lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
'''

#람다식
add = lambda a,b: a+b
result = add(3,4)
print(result)
#def식
def add(a,b):
	return a+b
#둘은 같은 알고리즘

#lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

