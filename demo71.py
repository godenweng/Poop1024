sales = [('vivo', 10), ('oppo', 5), ('asus', 3), ('lenovo', 20), ('nokia', 15)]


def explain(x):
    print(type(x))
    print(x[0], x[1])
    return x[1]


sales.sort(key=lambda x: x[0])
print(sales)
sales.sort(key=lambda x: x[1])
print(sales)
print("---------")
sales.sort(key=explain)
print(sales)

k1 = 'xyz'
k2 = b'xyz'
print(type(k1), type(k2))

