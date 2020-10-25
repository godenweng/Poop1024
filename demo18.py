import ast
y1 = "None"
y2 = None
y3 = None
print(type(y1), type(y2), y2 == y3, y2 is y3, y1 == y2, y1 is not y2)

x1 = "None"
x2 = "None"
# x2 = 5000
x3 = "None"
# x3 = "2+5**2"
z1 = ast.literal_eval(x1)
print(z1,type(z1))

z2 = None if x2 == "None" else x2
print(z2,type(z2))

z3 = eval(x3)
print(z3,type(z3))