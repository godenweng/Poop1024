def getDigit(x):
    returnDigit = 0
    while x > 0:
        x //= 10
        returnDigit += 1
    return returnDigit

print(getDigit(10))
print(getDigit(100))
print(getDigit(1000))
print(getDigit(10000))