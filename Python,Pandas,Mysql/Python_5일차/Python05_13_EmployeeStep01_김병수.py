TName = ["구분","사원명","입사일","급여"]

empInfo =[
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]
empPayTable = [
	[250,10],	[200,12],	[300,9],	[230,11],	[150,12]
]
print("구분\t사원명\t입사일\t급여")
print("-"*30)
for i in range(len(empInfo)):		# len(여기 안에 리스트를 넣으면 리스트의 크기를 알려줍니다)
	a = empPayTable[i][0] * empPayTable[i][1]

	if empInfo[i][0][0]=="T" or empInfo[i][0][0] == "t":
		print("계약직\t %s \t %s \t %d" %(empInfo[i][1],empInfo[i][2],a)) 
	elif empInfo[i][0][0]=="R" or empInfo[i][0][0] == "r":
		print("정규직\t %s \t %s \t %d" %(empInfo[i][1],empInfo[i][2],a)) 



	