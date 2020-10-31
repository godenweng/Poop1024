def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Sorry, input number should be an integer")
    if not number >= 0:
        raise ValueError("Sorrry,number should be positive")

    def inner_factorial(n):
        if n <= 1:
            return 1
        return n * inner_factorial(n - 1)

    return inner_factorial(number)


#print(factorial(-1))
print(factorial(5))
## 5*4*3*2*1 = 120
