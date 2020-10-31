def myException(level):
    if level < 1:
        raise Exception('some reason','some detail','some more detail..')

try:
    myException(0)
except Exception as e:
    print("oops got an error",e)
    for arg in e.args:
        print("argument =", arg)