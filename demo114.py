import multiprocessing
import sys
import time


def func1_exit_error():
    sys.exit(1)


def func2_normal():
    return


def func3_return_not_work():
    return 500


def func4_will_sleep():
    time.sleep(3)


def func5_exception_will_raise():
    raise RuntimeError("I made this error")


if __name__ == '__main__':
    jobs = []
    for f in [func1_exit_error, func2_normal, func3_return_not_work, func4_will_sleep]:
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()
        # jobs[-1].terminate()
    for j in jobs:
        j.join()
        print("%s exit code =%s " % (j.name, j.exitcode))

    for f in [func5_exception_will_raise]:
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()
