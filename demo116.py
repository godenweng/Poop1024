import logging
import  multiprocessing
import sys

def worker():
    print("doing some works")
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()