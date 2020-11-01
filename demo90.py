from collections import UserDict


class MyOwnDict(UserDict):
    def __init__(self, data={}, **kwargs):
        super().__init__()
        self.update(data)
        self.update(kwargs)
        pass

    def __add__(self, other):
        self.data.update(other)
        return self

    pass


a = MyOwnDict(a=1)
b = MyOwnDict(data={'b': 2})
c = MyOwnDict(c=3, d=4)
d = MyOwnDict(data={'e': 5, 'f': 6})

print(a)
print(b)
print(c)
print(d)
print(a + b)
print(a + b + c)
print(a + b + c + d)
