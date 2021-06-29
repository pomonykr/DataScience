menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
memList = []
print("="*17," 메뉴선택 " ,"="*17)

for i in range(len(menu)):
	print(menu[i],end=" ")
print()
print("1. 회원가입 2. 로그인 3. 회원목록 9. 메뉴종료")

print("="*46)
n = 0
while True:
	
	print("메뉴의 번호를 선택해주세요. : ", end='')
	a=int(input())
	if a == 1:
		print("SignUp")
		for i in range(len(itemList)):
			b =input("%s : " %itemList[i])
			memList.append(b)	
	elif a== 9:
		break
	else:
		print("번호를 다시 확인하세요")
	
	print(memList)
	n=n+1
	print("현재 회원수는 %s명 입니다."%n)


	