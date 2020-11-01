def func75():
    x =1
    y =2
    z=3
    yield x
    yield y
    yield z

print(type(func75()))
print(type(func75))
p1 = func75()
p2 = func75

print(next(p1))
print(next(p1))
print(next(p1))

