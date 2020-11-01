import functools
def my_oreo(func):
    @functools.wraps(func)
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")
    return wrapper

@my_oreo
def add_filling():
    print("butter_cream!")


add_filling()
print(repr(my_oreo))
print("----------")
print(repr(add_filling))
