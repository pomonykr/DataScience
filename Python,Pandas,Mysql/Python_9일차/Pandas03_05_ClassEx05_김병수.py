'''
생성자 (Constructor)
상속 : 일반화
**클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에
상속할 클래스 이름을 넣어주면 된다.
형식 ] class 클래스 이름(상속할 클래스 이름)
'''
class FourCal:
	def __init__(self,first,second):
		self.first = first
		self.second = second

	
	def sum(self,bbb):
		result = self.first + self.second
		return result
class MoreFourCal(FourCal):
	
	
	def pow(self,aaa):
		result = aaa**2
		return result

a = MoreFourCal(4,2)

print(a.pow(5))
print(a.sum())

a= MoreFourCal(2,7)
	