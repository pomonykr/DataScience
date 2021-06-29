#다른주소를 가리키도록 만들수는 없을까?
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a,"\t",b)

from copy import copy #import 미리 만들어진 외부에있는걸 끌어옴
a = [1,2,3]
b = copy(a) #copy를 사용하면 원래 있던것과 다른 주소값이 적용됨
print(b)
print(id(a))
print(id(b))
