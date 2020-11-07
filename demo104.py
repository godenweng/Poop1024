import doctest

def square(x):
    """ Ret run square of x
    >>> square(5)
    25
    >>> square(-5)
    25

    :param x:
    :return:
    """
    return x ** 2

if __name__ == '__main__':
    doctest.testmod()