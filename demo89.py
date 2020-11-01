from collections import UserList


class MyOwnList(UserList):
    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value

    def square(self):
        for i in range(len(self.data)):
            self.data[i] = self.data[i] ** 2


l1 = MyOwnList()
for p in range(10):
    l1[p] = 3 * p
print(l1)
l1.square()
print(l1)
l1.square()
print(l1)
