l1 = list('ABCDE')
l2 = ['Apple','Banana','Cookie','甜甜圈','早餐茶']
for l in l1:
    print(l)
for l in l2:
    print(l)
    for c in l:
        print(c)

print('A' in l1, 'A' not in l1)
print('A' in l2, 'A' not in l2)
print('Apple' in l2, 'Apple' not in l2)

print('C index=',l1.index('C'))
print('Cookie index=',l2.index('Cookie'))

print('C count=',l1.count('C'))
print('Z count=',l1.count('Z'))

