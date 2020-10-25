import sys

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a + b

    # print(result)
    return result

if __name__ == '__main__':
    print(sys.argv[-1])
    fib(int(sys.argv[-1]))
