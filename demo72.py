class class72:
    def __init__(self, low, high):
        print("object createed")
        self.current = low
        self.high = high
        pass

    def __iter__(self):
        print("object begin to iterate")
        return self

    def __next__(self):
        print("object call next")
        if self.current > self.high:
            raise StopIteration()
        else:
            self.current += 1
            return self.current - 1


c1 = class72(10, 20)
for c in c1:
    print("first time iteerate",c)
print("----------------------------")
for c in c1:
    print("first time iteerate",c)
print("---------------------------")
c2 = class72(5, 15)
print(next(c2))
print(next(c2))
print(next(c2))
print("-----------------------------")
# pass
# print(next(c1))
