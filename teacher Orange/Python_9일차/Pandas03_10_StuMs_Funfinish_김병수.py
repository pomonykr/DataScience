menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],[89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
#1문제:
for jj in range(len(idList)):
	dic[idList[jj]]=scoreList[jj]

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


def num2():		
	print(menu[1])
	d=input("추가등록 하는 학생의 이름을 적어주세요: ")
	if d in deleteIDList:
		print("탈퇴한 학생은 다시 가입할수 없습니다")
	elif d in dic:
		print("이미 가입한 학생입니다")
	else:	
		o=int(input("필기점수를 입력하세요: "))
		p=int(input("실기점수를 입력하세요: "))
		r=int(input("인성점수를 입력하세요: "))
		dic[d] = [o,p,r]



def num3():
		print(menu[2])
		for ML in range(len(MenuList)):
			print(MenuList[ML],end='\t')
		print()	
		print("-"*80)
		for j in dic.keys():
			aver = sum(dic[j]) / len(scoreList[0])
			p = "합격" if aver >= 70 else "불합격"

			print("%s\t%d\t%d\t%d\t%d\t%.2f\t%s"%(j,dic[j][0],dic[j][1],dic[j][2],sum(dic[j]),aver,p))

while True:
	n = input("\t메뉴의 번호를 선택하세요 : \t")
	n=int(n)
	if n==1:
		d=input("탈퇴하는 학생의 이름을 적어주세요 : ")
		if d in dic:
			del dic[d]
			deleteIDList.append(d)
			print("탈퇴한 학생 : ",deleteIDList)
		else:
			print("이름을 확인해주세요")
	elif n == 2:	
		num2()
	elif n == 3:
		num3()
	elif n== 9:
		print("안녕히가세요 또오세요")
		break
	elif n == 4:
		for j in dic.keys():
			aver = sum(dic[j]) / len(scoreList[0])
			if aver >= 70:
				print("80점 이상 합격자는 %s 입니다"%j)
	else:
		print("입력 번호를 확인하세요")

			
