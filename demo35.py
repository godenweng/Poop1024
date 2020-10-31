l1 = list('ABCDE')
l1.insert(0,'*')
print(l1)
print(hex(id(l1)))
l1.insert(2,'$')
print(l1)
l1.insert(4,'!')
print(l1)
print(hex(id(l1)))

l1.remove('*')
print(l1)
l1.remove('$')
print(l1)
l1.remove('!')
print(l1)


l3 = list('ABCD****')
print(l3)
for _ in range(l3.count('*')):
    l3.remove('*')
print(l3)