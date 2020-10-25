l1 = []
l2 = ['a','b','c']
l3 = list('abc')
print(l2,l3,l2 ==l3)
l4 = [1,2,3]
l5 = [1,'b',[3,4],None,{'5'}]
print(l4)
print(l5)
print(type(l4),type(l5))
print(len(l1),len(l2),len(l3),len(l4),len(l5))
print(l4 == l5,l4 != l5)
print(l4[1] ==l5[1],l4[1] !=l5[1])
print(l4[int(1.0)])