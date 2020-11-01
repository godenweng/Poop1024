import time


def my_timer(func):
    def wrapper_timer(*args, **kwargs):
        print("start timer")
        startTime = time.perf_counter()
        value = func(*args, **kwargs)
        endTime = time.perf_counter()
        print("stop timer")
        print(f"{func.__name__} total cost {endTime - startTime} seconds")
        return value

    return wrapper_timer


@my_timer
def spend_time_to_calculate(times=10,upper_range=1000):
    total = 0
    for _ in range(times):
        total = sum([i ** 2 for i in range(100)])
    return total


print("calculate result ={}".format(spend_time_to_calculate(times=10,upper_range=1000)))
