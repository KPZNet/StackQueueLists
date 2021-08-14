
from Stacks import StackLinkedList
from Stacks import StackList
from Queues import QueueLinkedList
from Queues import QueueList

import threading


import time

NANO_TO_MS = 1000000




class StackRunner:
    def __init__(self):
        self.ls = StackList()
        self.lls = StackLinkedList()
        self.ls_timing = 0.0
        self.lls_timing = 0.0
        self.threadLock = threading.Lock ()
        self.flagA = False


    def AddtoQueue(self, qu, thr, runs) :

        for k in range ( runs ) :
            self.threadLock.acquire()
            qu.enqueue ( k )
            print("Add Queue Size: {0}".format(qu.qsize()))
            self.threadLock.release ()
        self.threadLock.acquire()
        self.flagA = True
        self.threadLock.release ()

    def RemovefromQueue(self, qu, thr) :
        while self.flagA == False:
            self.threadLock.acquire()
            qu.dequeue()
            print("Remove Queue Size: {0}".format(qu.qsize()))
            self.threadLock.release()



    def RunThreadedQueues(self):
        try :
            q = QueueList ()
            start_time = time.perf_counter_ns()
            t1 = threading.Thread ( target=self.AddtoQueue, args=(q, "Thread-1", 1000000) )
            t1.start()

            t2 = threading.Thread ( target=self.RemovefromQueue, args=(q, "Thread-2") )
            t2.start()
            stop_time = time.perf_counter_ns()
            self.ls_timing = (stop_time - start_time) / NANO_TO_MS

            t1.join()
            t2.join()

            return self.ls_timing

        except :
            print ( "Error: unable to start thread" )


    def RunQueueList(self, runs, size, qu):
        print("<<< Queue List RunTimes >>>")
        ll = qu

        start_time = time.perf_counter_ns ()

        for k in range(runs):
            for i in range ( size ) :
                ll.enqueue ( i )

            for j in range ( size ) :
                ll.dequeue ()

        stop_time = time.perf_counter_ns ()
        self.ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  self.ls_timing

    def RunQueueList2(self, runs, size, deqs, qu):
        print("<<< Queue List RunTimes >>>")
        ll = qu

        start_time = time.perf_counter_ns ()

        for i in range ( size ) :
            ll.enqueue ( i )

        for k in range(runs):
            for i in range ( deqs ) :
                ll.enqueue ( i )

            for j in range ( deqs ) :
                ll.dequeue ()

        stop_time = time.perf_counter_ns ()
        self.ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  self.ls_timing





if __name__ == '__main__' :

    sr = StackRunner()

    tm = sr.RunThreadedQueues()
    print("Thread Time: {0}".format(tm))

    exit(0)


    lq_time = sr.RunQueueList(10000, 1000, QueueList())
    llq_time = sr.RunQueueList ( 10000, 1000, QueueLinkedList () )
    print ( "RunA List Type: {0}  vs. LinkedList Type: {1}".format(lq_time, llq_time) )

    lq_time = sr.RunQueueList(10000, 5, QueueList())
    llq_time = sr.RunQueueList ( 10000, 5, QueueLinkedList () )
    print ( "RunB List Type: {0}  vs. LinkedList Type: {1}".format(lq_time, llq_time) )

    lq_time = sr.RunQueueList2(10000, 500, 5, QueueList())
    llq_time = sr.RunQueueList2 (10000, 500, 5, QueueList())
    print ( "RunB List Type: {0}  vs. LinkedList Type: {1}".format(lq_time, llq_time) )




