menu=['orange','straw','peach','mango','grape','종료']
price=['1000','2500','1500','2000','2000','6번을 누르세요']

while True:
	for i in range(len(menu)):
		print("%d: %s\t:\t%s"%(i+1,menu[i],price[i]))
		
#	print("======================================")
#	print("1.orange		:	1000원")
#	print("2.strawberry		:	2500원")
#	print("3.peach			:	1500원")
#	print("4.mango			:	2000원")
#	print("5.grape			:	2000원")
#	print("6.종료	")
#	print("======================================")
	
#	result= int(input("번호를 입력하세요 : "))
#	if result == 1:
#		print("orange 1000원 입니다")
#	elif result == 2:
#		print("strawberry 2000원 입니다")
#	elif result == 3:
#		print("peach 1500원 입니다") 
#	elif result == 4:
#		print("mango 2000원 입니다")
#	elif result == 5:
#		print("grape 2000원 입니다")
#	elif result == 6:
#		print("다음에 또오세요")
#		break

	result= int(input("원하시는 과일번호를 입력하세요 : "))
	if result == 1:
		print("%s %s 원 입니다"%(menu[result-1],price[result-1]))
	elif result == 2:
		print("%s %s 원 입니다"%(menu[result-1],price[result-1]))
	elif result == 3:
		print("%s %s 원 입니다"%(menu[result-1],price[result-1])) 
	elif result == 4:
		print("%s %s 원 입니다"%(menu[result-1],price[result-1]))
	elif result == 5:
		print("%s %s 원 입니다"%(menu[result-1],price[result-1]))
	elif result == 6:
		print("안녕히가세요 또오세요")
		break