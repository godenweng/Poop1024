import multiprocessing
import time


def daemon():
    name = multiprocessing.current_process().name
    print("daemon:%s start" % name)
    time.sleep(2)
    print("daemon:%s stop" % name)


def nonDaemon():
    name = multiprocessing.current_process().name
    print("non daemon:%s start" % name)
    time.sleep(2)
    print("non daemon:%s stop" % name)


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    n = multiprocessing.Process(name='non daemon', target=nonDaemon)
    n.daemon = False
    print("daemon is alive?",d.is_alive())
    print("nonDaemon is alive?",n.is_alive())
    print("====================")
    d.start()
    n.start()
    print("[2]daemon is alive?",d.is_alive())
    print("[2]nonDaemon is alive?",n.is_alive())
    d.terminate()
    n.terminate()
    print("[3]daemon is alive?",d.is_alive())
    print("[3]nonDaemon is alive?",n.is_alive())
    time.sleep(0.1)
    print("[4]daemon is alive?",d.is_alive())
    print("[4]nonDaemon is alive?",n.is_alive())