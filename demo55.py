n = 200
summation = 0
counter = 1
maximum = 30000

while counter <= n:
    summation += counter
    counter += 1
    if summation > maximum:
        break
else:
    print("calculate terminated")

print("total={}".format(summation))
