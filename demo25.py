x = 5
print(x)
print(y := 6)

inputs = list()
MESSAGE1 = "write something first (quit）: "
current = input(MESSAGE1)
while current != "quit":
    inputs.append(current)
    current = input(MESSAGE1)

print(inputs)
