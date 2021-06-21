
for i in range(1,6):
	for j in range(0,i):
		print("*",end='')
	print()

#역순의 별찍기를 해보세요

for i in range(1,6):
	for j in range(i,6):
		print("*",end='')
	print()

#다른형식

for i in range(1,6):
	print(' '*(5-i)+"*"*i)

for i in range(1,6):
	print(' '*(i-1)+"*"*(6-i))