inputs = list()
MESSAGE1 = "write something first (quit）: "
while (current := input(MESSAGE1)) != "quit":
    inputs.append(current)

print(inputs)
