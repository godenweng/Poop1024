x1 = 5
x2 = x1
print(x1, x2)
print(hex(id(x1)), hex(id(x2)))
x1 = 6
print(hex(id(x1)), hex(id(x2)))
l1 = [5]
l2 = l1
print(l1, l2)
print(hex(id(l1)), hex(id(l2)))
l1[0] = 6
print(l1, l2)
print(hex(id(l1)), hex(id(l2)))


def addSomethig(para):
    para.append("Zebra")

animals = ['alpace', 'baboon']
print(animals)
addSomethig(animals)
print(animals)
