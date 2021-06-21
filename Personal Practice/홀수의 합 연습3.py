#1~10 까지의 홀수합 출력!!
odd=0
even=0
#for i in range(1,11,2):
#	odd = odd+i
#print(odd)
 #다른방법으로 해보세요~!
a = 0
b = 0
for i in range(1,11):
	if i % 2 == 1:
		a = a+i
print("1~10까지의 홀수의 합은 : ",a)

for j in range(1,11):
	if j % 2 == 0:
		b = b+j
print("1~10까지의 짝수의 합은 : ",b)