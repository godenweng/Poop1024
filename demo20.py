from typing import Union


def twice(number):
    return 2 * number


print(twice(2.54))
print(twice(500))
print(twice("500"))


def twice2(number: Union[float, int]) -> float:
    return 2 * number


print(twice2(2.54))
print(twice2(500))
print(twice2("500"))
