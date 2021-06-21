import random

print("이번주의 로또 당첨번호 : ")
for i in range(7):
	print("%d " %random.randint(1,45),end='')
	print()
