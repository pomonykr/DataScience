a = [1,2,3]
b = a

print("a, b 변경전 = " , a ,"/ ", b)
b[1] = 4
print("a[1] 변경후 = ", a ,"/ ", b)


c= 4
d =c
c=5
print(id(c))
print(id(d))

print(c)
print(d)