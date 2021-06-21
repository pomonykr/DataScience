#score = input("점수를입력하세요 : ")
#if int(score) >= 80:
#	print("합격입니다")
#else:
#	print("다음기회에")

# input 을 이용하여 노력값이 99점 초과면 칭찬을 반환해줄것

No=input("노력값을 입력하세요 : ") 
a = "더 노력할수 있잖아요" if int(No) > 99 else "노오력하세요"
print(a)

