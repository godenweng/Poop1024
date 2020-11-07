import multiprocessing


def worker(num,header):
    print("[%s]worker with parameter：%d" % (header,num))

print("========\n")
if __name__ == '__main__':
    jobs = []
    for i in range(5):
        print("now process part : %d" % i)
        p = multiprocessing.Process(target=worker, args=(i,"ANOTHER_PROCESS"))
        jobs.append(p)
        p.start()
    print("jobs=", jobs)
