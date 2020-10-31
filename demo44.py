d1 = {'name': 'poop', 'level': 'entry', 'duration': 35}
d2 = {'name': 'poop', 'duration': 35, 'level': 'entry'}
print(type(d1), type(d2))
print(d1, d2)
print(d1 == d2, d1 is d2)
print(d1['name'] ,d1['duration'],d2['level'])
print('name'in d1,'duration' in d1,'lever' in d2)

