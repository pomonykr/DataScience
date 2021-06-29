#함수 안에서 선언한 변수의 효력 범위
#함수 안에서 사용하는 매개변수는 지역변수이다.

#함수 안에서 함수 밖의 변수를 변경하는 방법

a=1
def vartest(a):
	a = a+1
	print(a)
vartest(a)

print(a)
print("-"*20)