import functools
def my_oreo(func):
    @functools.wraps(func)
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")
    return wrapper

@my_oreo
def regular_filling():
    print("butter_cream!")

@my_oreo
def peanut_filling():
    print("coff_cream!")

fillings = [regular_filling,peanut_filling]

for f in fillings:
    print("--------")
    f()
print("========================")
print(repr(regular_filling))
print(repr(peanut_filling))
