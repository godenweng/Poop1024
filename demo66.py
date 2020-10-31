x = 'global'
y = 100
z = [3.14]


class Foo():
    def __init__(self, value):
        self.value = value


f1 = Foo(5)


def foo():
    global x
    global y
    print("[foo],x=", x, ", y=", y)
    x *= 2
    y *= 4
    z[0] = z[0] ** 2
    f1.value = f1.value *3

    print("[foo2], x=", x, ", y=", y,", f1=",f1.value)


print("-----------------")
print(x)
print("-----------------")
foo()
print("-----------------")
print(x)
print("-----------------")
print(x, y)
print("-----XYZ--------")
print(x, y, z)
print("-----XYZ--------")
print(x, y, z,f1.value)
