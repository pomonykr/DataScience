menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
a=[1, 2, [3, 4, 5], 2, 7, "ankl"]
for i in a:
	print(len(i))

print("="*17," 메뉴선택 " ,"="*17)

for i in range(len(menu)):
	print(menu[i],end=" ")
print()
#print("1. 회원가입 2. 로그인 3. 회원목록 9. 메뉴종료")

print("="*46)

while True:
	
	print("메뉴의 번호를 선택해주세요. : ", end='')
	a=int(input())
	if a in range(1,4):
		print("%s Algorithm Chk"%menu[a-1])
	elif a== 9:
		break
	else:
		print("번호를 다시 확인하세요")