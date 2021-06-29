A = 0 
M = 0
S = 0
G = 0

while True:
	num = int(input("10이상의 숫자를 입력하시오 : "))
	if num >= 10:
		print("10 이상의 숫자 확인하세요. ")
	elif(num==0):	
		print("종료!!")
		break
	else:
		print("10이상의 숫자를 확인하세요.")
		continue
    
	for i in range(1,u):
		if i % 3 == 0:
			print("apple")
		elif i % 4 == 0:
			print("melon")
		elif i % 5 == 0:
			print("grape")
		elif i % 8 == 0:
			print("strawberry")

