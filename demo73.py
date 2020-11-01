def infinate_generator(start=0):
    while True:
        yield start
        start += 2


for num in infinate_generator(5):
    print(num, end=" ")
    if num > 20:
        break
