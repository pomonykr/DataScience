menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],[89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;

def inputData():
	for jj in range(len(idList)):
		dic[idList[jj]]=scoreList[jj]
def PrintList():
	n = input("\t메뉴의 번호를 선택하세요 : \t")
	n=int(n)
	if n==3:
		print(menu[n-1])
		for ML in range(len(MenuList)):
			print(MenuList[ML],end='\t')
		print()	
		print("-"*80)
		for j in dic.keys():
			print("%s\t%d\t%d\t%d\t%d"%(j,dic[j][0],dic[j][1],dic[j][2],sum(dic[j])))
#1문제:
inputData()
#------------------
#		1문제:dic에 idList를 key값으로 하고, scoreList를 Value값으로
#		할당.
#-------------------

print("-"*80)
print("학생관리시스템 v01")
print("-"*80)
for i in range(len(menu)):
	print(menu[i],end=" ")
print()
print("-"*80)
#문제2.
PrintList()

			
for i in range(len(menu)):
	print(menu[i],end=" ")
print()
print("1. 회원가입 2. 로그인 3. 회원목록 9. 메뉴종료")

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
