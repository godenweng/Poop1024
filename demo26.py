inputs = list()
MESSAGE1 = "write something first (quit）: "
while True:
    current = input(MESSAGE1)
    if current == "quit":
        break
    inputs.append(current)

print(inputs)
