def my_oreo(func):
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")
    return wrapper

def add_filling():
    print("butter_cream!")

def add_filling111():
    print("coff_cream!")

getOreo = my_oreo(add_filling)
getOreo()
print( "---------------")
getOreo1 = my_oreo(add_filling111)
getOreo1()