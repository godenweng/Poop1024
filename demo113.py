import multiprocessing
import time
def demo_worker():
    print("start working")
    time.sleep(1)
    print("finish working")

if __name__ == '__main__':
    p = multiprocessing.Process(target=demo_worker)
    print("before start:",p)
    p.start()
    print("after start",p)
    #p.terminate()
    #print("just after terminate",p)
    time.sleep(0.01)
    print("after slepp:", p)
    p.join()
    print("joined",p)