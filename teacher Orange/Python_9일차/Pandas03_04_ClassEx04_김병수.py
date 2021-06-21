class FourCal :
	def __init__(self):
		pass
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result
		
	def sub(self):
		result = self.first - self.second
		return result

	def mul(self):
		result = self.first *self.second
		return result

	def div(self):
		result = self.first / self.second
		return result

a = FourCal(4,2)

print("%d + %d = %d"%(a.first,a.second,a.sum()))
print("%d - %d = %d"%(a.first,a.second,a.sub()))
print("%d * %d = %d"%(a.first,a.second,a.mul()))
print("%d / %d = %d"%(a.first,a.second,a.div()))