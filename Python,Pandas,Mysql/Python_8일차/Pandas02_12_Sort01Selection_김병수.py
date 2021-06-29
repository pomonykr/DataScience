a = [2,5,6,1,2,8,33,77,12]
for i in range(len(a)-1):
	for j in range(i+1,len(a)):
		if a[i] > a[j]:
			a[i],a[j] = a[j],a[i]
#	print("%d회차" %i, end=' ')
#	for k in a:
#		print(k, end= ' ')
#	print()
print("a의 오름차순은 : ",end = " " )
for p in range(len(a)):
	print(a[p],end=" ")
print()

a.reverse()
print("내림차순은 : ",a)