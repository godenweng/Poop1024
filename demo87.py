class Employee(object):
    def __init__(self):
        self.work = "work111"

    def dowork(self):
        print("working on: %s" % self.work)


class RD(Employee):
    def __init__(self):
        self.work = "Research*Development"


class FAE(Employee):
    def __init__(self):
        self.work = 'work with customers to solve issues'


class Scientist(Employee):
    def __init__(self):
        self.work = "do some AI"


print(RD.__bases__, FAE.__bases__, Scientist.__bases__)
print(Employee.__bases__)
r1 = RD()
r2 = FAE()
r3 = Scientist()
print('-----------------------')
r1.dowork()
r2.dowork()
r3.dowork()

print('-----------------------')
staffs = [r1, r2, r3]
for s in staffs:
    s.dowork()
