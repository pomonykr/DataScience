#교집합, 합집합 ,차집합을 구할 때이다.

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#1.교집합 동일한 결과 2가지 방법
inter1 = s1 & s2
inter2 = s1.intersection(s2)
print(inter1)
print(inter2)

print("-"*15)

