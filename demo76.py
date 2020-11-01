def my_oreo(func):
    def wrapper():
        print("upper side chocolate cookie")
        func()
        print("lower side chocolate cookie")
    return wrapper

def regular_filling():
    print("butter_cream!")

def peanut_filling():
    print("coff_cream!")

fillings = [regular_filling,peanut_filling]

for f in fillings:
    print("--------")
    getOreo = my_oreo(f)
    getOreo()

print( "=========================")
getOreo = my_oreo(peanut_filling)
getOreo()
print( "---------------")
getOreo1 = my_oreo(regular_filling)
getOreo1()