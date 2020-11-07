import  multiprocessing
import  time

def daemon():
    name = multiprocessing.current_process().name
    print("%s starting" % name)
    time.sleep(5)
    print("%s stop" % name)

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    d.start()
    d.join()