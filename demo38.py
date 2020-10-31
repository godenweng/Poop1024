v1 = 'ABCDE'
l1 = list(v1)
print(v1[:3],v1[2:])
print(l1[:3],l1[2:])
print(len(v1))
print(len(l1))
print([l for l in v1])
print([l for l in l1] )
l1[2] = 'c'
print(l1)
v1[2] = 'c'