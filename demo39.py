v1 = []
v2 = ()
v3 = {}
print(type(v1), type(v2), type(v3))
v4 = ['apple']
v5 = ['apple']
print(type(v4), type(v5))
v6 = [3, 4]
v7 = (3, 4)
print(type(v6), type(v7))
print(v6, v7)
v8 = ('a', 'b', 'c', 'd', 'e')
print(len(v8), v8[0], v8[4], v8[-1], v8[-5])
v9 = list('abcde')
print(v8, v9)
v9[2] = '*'
print(v8, v9)
#v8[2] = '*'
