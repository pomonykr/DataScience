#URL = https://search.naver.com/search.naver?
str1='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python'.split('?')
str2=str1[1]
strr=str2.split('&')
print('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python')
print('URL\nQuerystring\n')
#for i in strr:
#	print(i)
#print("Querystring 개수 : %d개"%len(strr))

print(strr[0][3])