import random
class MyException(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "MyException_str, value={}".format(self.value)

    def __repr__(self):
        return "MyException, value={}".format(self.value)
try:
    raise MyException(random.randint(10,100))

except MyException as error:
    print("MyException occurs")
    print("error =",error)
    print("error value=",error.value)
