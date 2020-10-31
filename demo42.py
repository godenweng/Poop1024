import copy

l1 = list('abcdef')
l2 = l1
l3 = l1[:]
l4 = copy.copy(l1)
l5 = copy.deepcopy(l1)
l6 = list(l1)
print(l1,hex(id(l1)) )
print(l2,hex(id(l2)))
print(l3,hex(id(l3)))
print(l4,hex(id(l4)))
print(l5,hex(id(l5)))
print(l6,hex(id(l6)))
l1[0] = 'A'
print( '======')
print(l1,hex(id(l1)))
print(l2,hex(id(l2)))
print(l3,hex(id(l3)))
print(l4,hex(id(l4)))
print(l5,hex(id(l5)))
print(l6,hex(id(l6)))


print("======================================================")
s1 = ['a','b']
s2 = ['c','d']
l1 = [s1,s2]
l2 = l1
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)
print(l1,hex(id(l1)))
print(l2,hex(id(l2)))
print(l3,hex(id(l3)))
print(l4,hex(id(l4)))
l1.append('*')
print(l1,hex(id(l1)))
print(l2,hex(id(l2)))
print(l3,hex(id(l3)))
print(l4,hex(id(l4)))

l1[0][0]='A'
print(l1,hex(id(l1)))
print(l2,hex(id(l2)))
print(l3,hex(id(l3)))
print(l4,hex(id(l4)))
