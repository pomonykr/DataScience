## 클래스 ##
#	틀 , 구조 -> 함수 + 속성(변수)
#	- 거푸집 :
#	- 객체 : 클래스로 부터 생성 
# 생성자 : 함수,클래스이름과 동일한 함수,주로 초기화

##클래스 사용
# - 객체 생성후 사용 -(객체.속성) (객체.함수)<-이런식으로 쓰임

class Fourcal:
	a = 1
	b = 2
	def rundata(self,one,two):
		self.one = a




	def setdata(self,first,second):
		self.first = first
		self.second = second

a = Fourcal()
a.setdata(4,5)
b.setdata(7,8)

print(a.first)
print(a.second)

print(b.first)
print(type(a))
