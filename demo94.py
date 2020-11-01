class MetaSingleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        print("[MetaSingleton]__call_")
        if self not in self._instances:
            print(f"{self.__class__} not exists,create one")
            self._instances[self] = super().__call__(*args, **kwargs)
            pass
        return self._instances[self]


class BankTicket(metaclass=MetaSingleton):
    pass

print("=============================")
t1 = BankTicket()
t2 = BankTicket()
print("BankTicket==>", t1 is t2, hex(id(t1)), hex(id(t2)))


class DriverFactory(metaclass=MetaSingleton):
    pass

print("=============================")
d1 = DriverFactory()
d2 = DriverFactory()
print("DriverFactory==>", d1 is d2, hex(id(d1)), hex(id(d2)))


class Bankchair:
    pass

print("=============================")
b1 = Bankchair()
b2 = Bankchair()
print(b1 is b2, hex(id(b1)), hex(id(b2)))
