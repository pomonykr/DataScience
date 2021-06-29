
while True:
	n = int(input("10이상의 숫자를 입력하시오 : "))
	if(n==0):	
		print("종료!!")
		break   
	elif n < 10:
		print("10 이상의 숫자 확인하세요. ") 
	fruitList = ["Apple","Melon","Grape","StrawBerry"]
	fruitNumber=[3,4,5,8]
	fruitCount=[0,0,0,0]

	print("== << %d 회 반복합니다. >>==" %N)
	for i in range(1, n+ 1):
		print("\n%2d. " %i , end="")
		for j in range(len(fruitList)):
			if(i % fruitNumber[j] == 0):
				fruitCount[j] += 1
				print("%s" % fruitList[j], end=" ")
	print("\n\n== << Fruit Count List >> ==")
	for i in range(len(fruitList)):
		print("%d. %-12s %2d회" % (i + 1, fruitList[i], fruitCount[i]))