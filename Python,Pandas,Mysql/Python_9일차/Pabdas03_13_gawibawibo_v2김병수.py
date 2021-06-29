import random

Pscore = 0
Cscore = 0
player = "가위"

while(player != "종료"):
	print("나 : ", Pscore, ":", "컴퓨터", Cscore)
	player = input("가위 , 바위 , 보 중에 하나를 선택하세요 (종료하려면 '종료'): ")
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
			Cscore = Cscore +1
		else:
			print("이겼다!")
			Pscore = Pscore+1
	elif (player == "보" ):
		if (computer == "바위"):
			print("이겼다!")
			Pscore = Pscore+1
		else:
			print("졌다!")
			Cscore = Cscore+1
	elif(player == "가위"):
		if (computer == "바위"):
			print("졌다!")
			Cscore = Cscore+1
		else:
			print("이겼다!")
			Pscore = Pscore+1


		
		
		
		