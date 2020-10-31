d1 = {'name': 'poop', 'duration': 35}
for key in d1:
    print(key, d1[key])
print("=========")
for key in d1.keys():
    print(key, d1[key])
print("=========")
for value in d1.values():
    print(value)
print("=========")
for item in d1.items():
    print(type(item), item)
    print(item[0], item[1])
print("=========")
for k,v in d1.items():
    print("key=",k,"value=",v)
print("=========")
print(d1['name'])
#print(d1['instructor'])
print(d1.get('name'),d1.get('duration'))
print(d1.get('instructor'))