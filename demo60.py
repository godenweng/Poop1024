def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError as error:
        print("divide by zero, error =",error)
    except TypeError as error:
        print('type Error')
    else:
        print("result ={}".format(result))
    finally:
        print("==> divide function executed")

divide(8,6)
divide(5,0)
divide(8,6)
divide(8,'6')