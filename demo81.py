def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate cookie")
        print(f"middle side {func(x)}")
        print("lower side chocolate cookie")
    return wrapper

@my_oreo
def add_filling(fill):
    return f"{fill}_cream!"


add_filling("chocolate")
