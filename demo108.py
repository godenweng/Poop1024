import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print("%s start " % name)
    time.sleep(2)
    print("%s stop " % name)

def myServer():
    name = multiprocessing.current_process().name
    print("%s start " % name)
    time.sleep(6)
    print("%s stop " % name)

if __name__ == '__main__':
    w0 = multiprocessing.Process(target=myServer, name="Query Service")
    w1 = multiprocessing.Process(target=worker)
    w2 = multiprocessing.Process(target=worker, name="Garbage Collector Process")
    w3 = multiprocessing.Process(target=worker)
    w0.start()
    w1.start()
    w2.start()
    w3.start()

