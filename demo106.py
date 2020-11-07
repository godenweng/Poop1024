import multiprocessing
import time


def worker():
    print("working....")
    time.sleep(5)
    print("done.....")
    return

def worker1():
    print("work1ing....")
    time.sleep(5)
    print("done1.....")
    return

def worker2():
    print("work2ing....")
    time.sleep(5)
    print("done2.....")
    return

workers = [worker, worker1, worker2]

if __name__ == '__main__':
    jobs = []
    for i in range(3):
        print("now execute part :%d" % i)
        p = multiprocessing.Process(target=workers[i])
        jobs.append(p)
        p.start()
    print("result=", jobs)
    print("program terminated")
