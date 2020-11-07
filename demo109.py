import  multiprocessing
import  time

def daemon():
    name = multiprocessing.current_process().name
    print("daemon:%s start" % name)
    time.sleep(3)
    print("daemon:%s stop" % name)

def nonDaemon():
    name = multiprocessing.current_process().name
    print("non daemon:%s start" % name)
    time.sleep(3)
    print("non daemon:%s stop" % name)

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon',target=daemon)
    d.daemon = True
    n = multiprocessing.Process(name='non daemon',target=nonDaemon)
    n.daemon = False
    d.start()
    n.start()
    #time.sleep(4)
    print("main process terminated")