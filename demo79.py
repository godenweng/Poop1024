def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate cookie")
        func(x)
        print("lower side chocolate cookie")
    return wrapper



@my_oreo
def add_filling(fill):
    print(f"{fill}_cream!")


add_filling("vanilla_chocolate")
