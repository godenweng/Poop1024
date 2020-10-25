import  demopkg
import  demopkg.demokg2

def fib(n):
    print(demopkg.GLOBAL1)
    print(demopkg.demokg2.GLOBAL2)
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == '__main__':
    fib(500)