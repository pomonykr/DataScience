marks = [90,25,67,45,80]

a=0

for mark in marks:
	a=a+1
	if mark < 60:
		continue
	print(a , "번 학생 축하합니다. 합격입니다.")

#number을 없애고 같은형식으로 출력하시오 -->실패

#for mark in marks:
#	if mark < 60:
#		continue
#	print("%d번 학생 축하합니다. 합격입니다."%len(marks[))
