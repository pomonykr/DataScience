import random

Pscore = 0
Cscore = 0
a =[0,0]
player = "가위"
resultList=[]

print("*"*60)
print("컴퓨터와 함께하는 가위바위보 대결 (5판 3선승후 자동종료)")
print("*"*60)

while True:
	
	
	player = input("가위 , 바위 , 보 중에 하나를 선택하세요 : ")
	number	 = random.randint(0,2)
	if (number == 0):
		computer = "가위"
	elif (number == 1):
		computer = "바위"
	else:
		computer = "보"
	print("사용자 : " , player, ":" , "컴퓨터: " ,computer)
	
	if (player == computer):
		print("비겼다! " )
	elif (player == "바위" ):
		if (computer == "보" ):
			print("졌다!")
			a[1] = a[1] +1
			print("%d승 %d패"%(a[0],a[1]))
		else:
			print("이겼다!")
			a[0] = a[0]+1
			print("%d승 %d패"%(a[0],a[1]))
	elif (player == "보" ):
		if (computer == "바위"):
			print("이겼다!")
			a[0] = a[0]+1
			print("%d승 %d패"%(a[0],a[1]))
		else:
			print("졌다!")
			a[1] = a[1]+1
			print("%d승 %d패"%(a[0],a[1]))
	elif(player == "가위"):
		if (computer == "바위"):
			print("졌다!")
			a[1] = a[1]+1
			print("%d승 %d패"%(a[0],a[1]))
		else:
			print("이겼다!")
			a[0] = a[0]+1
			print("%d승 %d패"%(a[0],a[1]))
	if a[0] == 3:
		print("휴먼 승리!")
		break
	elif a[1] == 3:
		print("콤퓨타 승리!")
		break

		