def outer():

    x = "local"
    def inner():
        nonlocal  x
        print("[inner0]x =", x)
        x = "non local"
        print("[inner]x =", x)

    print("[outer1]x=",x)
    inner()
    print("[outer2]x=", x)

outer()
