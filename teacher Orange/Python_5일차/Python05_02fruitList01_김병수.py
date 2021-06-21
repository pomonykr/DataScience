
while True:
	n = int(input("10이상의 숫자를 입력하시오 : "))
	if(n==0):	
		print("종료!!")
		break   
	elif n < 10:
		print("10 이상의 숫자 확인하세요. ") 
	answer=[]
	fruitCnt=[]
	if n >= 10:
		print("==<< %d번 반복합니다. >>==" % n)
		for i in range(1,n+1):
			if i % 3 == 0:
				answer.append("Apple")
			if i % 4 == 0:
				answer.append("Melon")
			if i % 5 == 0:
				answer.append("Grape")
			if i % 8 == 0:
				answer.append("StrawBerry")
			fruitCnt += answer
			if len(answer) == 0:
				print("%d." % i)
			else:
				print("%d.		%s" %(i,answer))
			answer = []
		print("==<< Fruit Counter List >>==")
		print("Apple : %d회" %fruitCnt.count("Apple"))
		print("Melon : %d회" %fruitCnt.count("Melon"))
		print("Grape : %d회" %fruitCnt.count("Grape"))
		print("StrawBerry : %d회" %fruitCnt.count("StrawBerry"))