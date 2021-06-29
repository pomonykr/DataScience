'''
Value 리스트 만들기 (values)
'''
a = {'name':'pay','phone':'0119993323','birth':'1118'}

print(a.values())

print("-"*15)

#Key,Value 쌍 얻기(items)
print(a.items())
print("-"*15)

#Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)