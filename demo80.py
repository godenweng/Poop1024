def my_oreo(func):
    def wrapper(*x):
        print("upper side chocolate cookie")
        func(*x)
        print("lower side chocolate cookie")
    return wrapper

@my_oreo
def add_multi_filling(*fills):
    for fill in fills:
        print(f"{fill}_cream!")


add_multi_filling()
print('------')
add_multi_filling('chocolate')
print('------')
add_multi_filling('chocolate','vanilla','coff')
print('------')
fills = ['strawberry','pineapple','peach']
add_multi_filling(*fills)