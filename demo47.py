sales = ['iphone11', 'iphone12', 'iphone12', 'iphone12 pro', 'iphone12', 'iphone12', 'iphone12 pro', 'iphone11',
         'iphone11', 'iphone12', 'iphone12','apple watch','apple SI book']
count = {}
#count = {'iphone11': 0, 'iphone12': 0, 'iphone12 pro': 0}

for sale in sales:
    count.setdefault(sale,0)
    count[sale] += 1
print(count)

print( "========================")
count2 = {}
sales2 =[('iphone11',10),('iphone12',10),('iphone12 pro',20),
('iphone11',20),('iphone12',5),('iphone12 pro',15),('iphone12 pro',25),('iphone12 pro',35)]

for item, quantity in sales2:
    count2.setdefault(item,0)
    count2[item] += quantity
print(count2)

print( "========================")
count3 = {}
sales3 =[('iphone11',10,2),('iphone12',10,1),('iphone12 pro',20,2)]

for item, quantity,tt in sales3:
    count3.setdefault(item,0)
    count3[item] += quantity
    conut3[item] += tt

print(count2)