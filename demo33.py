l1 = ['a','b','c']
print(l1+l1)
print(l1 *3)
print(3 *l1)
print(l1)
print(l1 + [3])
del l1[2]
print(l1)

l2 = ['abc']
print(l2+l2)
print(l2 *3)
print(3 *l2)
print(l2)
print(l2 + [3])


l3 = ['a','b','c']
l3.append('d')
print(l3)
l4 = ['a','b','c']
l4 = l4 + ['d']
print(l4)
print(hex(id(l3)))
print(hex(id(l4)))
print(l3 == l4,l3 is l4)
