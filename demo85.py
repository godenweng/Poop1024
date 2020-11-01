class Layout1:
    pass

class Layout2(object):
    pass

l1 = Layout1()
l2 = Layout2()

print(type(Layout1),type(Layout2),type(int))

print(type(l1),type(l2))
print(type(l1).__name__,type(l2).__name__)
print(l1.__class__.__name__,l2.__class__.__name__)

print(type(l1) == l1.__class__,type(l2) == l2.__class__)

print(Layout1.__bases__,Layout2.__bases__)