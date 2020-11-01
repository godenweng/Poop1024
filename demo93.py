class SimpleMeta(type):
    def __new__(cls, clsname, superclass, attributedict):
        print("[simpleMeta]{__new__} called")
        print(f"class name={clsname}")
        print(f"parent class name={superclass}")
        print(f"attribute:{attributedict}")
        return type.__new__(cls, clsname, superclass, attributedict)

    def __call__(self, *args, **kwargs):
        print("[SimpleMeta]{__call__} called")
        for arg in args:
            print("get a parameter:{}".format(arg))
        return super().__call__(*args, **kwargs)


class S:
    def __init__(self, name, age):
        print("__init_ from s")
        self.name = name
        self.age = age


class A(S, metaclass=SimpleMeta):
    def __init__(self,name,age):
        print("__init__ from a")
        super().__init__(name,age)
        print("__init__ custom action from a")
    pass


print("instinate S1 and a1")
s1 = S('james', 20)
a1 = A('mark', 43)
a2 = A('abby', 34)
print(s1.__class__, a1.__class__, a2.__class__)
print(s1.__class__.__bases__, a1.__class__.__bases__)
