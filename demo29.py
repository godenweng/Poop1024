x = 5
y = 5
print(hex(id(x)), hex(id(y)))
x = 6
print(hex(id(x)), hex(id(y)))
y = 6
print(hex(id(x)), hex(id(y)))
l1 = ['a', 'b']
l2 = l1
l3 = ['a', 'b']
print(hex(id(l1)))
print(hex(id(l2)))
print(hex(id(l3)))
print(l1 == l2, l1 == l3) #true true
print(l1 is l2, l1 is l3) #true false
