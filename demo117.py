import threading
import time
import sys


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        # super().__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("start a thread:", self.name)
        sys.stdout.flush()
        time.sleep(5)
        print("stop a thread", self.name)
        sys.stdout.flush()


t1 = myThread(1, "Thread-1", 1)
t2 = myThread(2, "Thread-2", 2)
t1.start()
t2.start()
t1.join()
t2.join()
print("program terminated")
