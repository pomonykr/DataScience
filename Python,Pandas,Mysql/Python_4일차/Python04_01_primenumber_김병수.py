while True:
	so=int(input("20이상의 수를 입력하세요 : "))

	if so == 0:
		exit()
	elif so < 20:
		print("숫자 확인하세요")
		continue
	else:
		print()

	for i in range(so+1):
		result='O'
		if i <2 :
			result = 'X'
		for j in range(2,i):
			if i%j == 0:
				result = 'O'
		print("%d 소수 %s" %(i,result))
		if result:
			print(i, end=" ")


#	#range(초기 설정하는 수,여기까지 반복할게요,숫자 증가하는 범위(안적 자동+1)
#	for i in range(1,so+1):
#		# 여기서 변수를 초기화
#		chk = 'X'
#		if i < 2:
#			print("%d 소수 %s" %(i,chk))
#			chk = 'O'
#			continue
#		for j in range(2,i):
#			if i % j == 0:
#				chk = 'X'
#		print("%d 소수 %s" %(i,chk))
           
#a = 0
#for i in range(2,so):
#	if i % 2 == 0:
#		a = i
#	elif i % 3 == 0:
#		a = i
#	else:
#		continue
#
#	print(a)







		