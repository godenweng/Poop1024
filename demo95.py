class SingletonParent(object):
    _instance = None

    def __init__(self):
        print("[singletonParent] init is called " )

    def __new__(cls, *args, **kwargs):
        print("[new] is called")
        if not cls._instance:
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

class RegularClass():
    pass

class SingletonClass(SingletonParent):
    pass
print("===================")
r1 = RegularClass()
r2 = RegularClass()
print(r1 is r2, hex(id(r1)),hex(id(r2)))
print("===================")
s1 = SingletonClass()
s2 = SingletonClass()
print(s1 is s2, hex(id(s1)),hex(id(s2)))