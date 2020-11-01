def make_increment(n):
    return lambda x: x + 2 * n

add10 = make_increment(10)
print(add10(10),add10(20),add10(30))
add5 = make_increment(5)
print(add5(10),add5(20),add5(30))
print(make_increment(10)(20))
print(type(make_increment))
print(type(make_increment(20)))


def make_tuple(p):
    return lambda x: (x, 'P' * p)

l1 = lambda p, q, r: p + q + r
print(l1(3, 4, 5))

l2 = lambda *args: [p for p in args]
print(l2("app","org","ban","kiwi"))


t5 = make_tuple(5)
print(t5('Apple'),t5('Banana'),t5('cookie'))
t3 = make_tuple(3)
print(t3('ice'))
print(make_tuple(10)('ice cream'))


