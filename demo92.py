from abc import ABC, abstractmethod

class A1(ABC):
    def __init__(self,value):
        super().__init__()
        self.value = value
 

    @abstractmethod
    def do_something(self):
        pass

class B1(A1):
    def do_something(self):
        print("working....")

class C1(A1):
    pass

# a1= A1(5)

b1 = B1(5)
b1.do_something()
# c1 = C1(5)
print(type(A1))
print(type(B1))
print(type(C1))