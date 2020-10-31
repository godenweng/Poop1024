v1 = ['a','b','c']
v2 = ['a','b','c']
print(type(v1),type(v2))
v1.append('d')
x1 = tuple(v1)
x2 = list(v2)
print(type(x1),type(x2))
x2.append('d')
print(x1,x2)