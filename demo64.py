def outer(number1):
    def inner_increment(n):
        return n + 1

    number2 = inner_increment(number1)
    print(number1, number2)

outer(100)
