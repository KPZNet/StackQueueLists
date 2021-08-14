
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

    def AddtoQueue(self, qu, thr, runs, size) :
        for k in range ( runs ) :
            for i in range ( size ) :
                self.threadLock.acquire()
                qu.enqueue ( i )
                self.threadLock.release ()

    def RemovefromQueue(self, qu, thr, runs, size) :
        for k in range ( runs ) :
            for i in range ( size ) :
                self.threadLock.acquire ()
                qu.dequeue ( )
                self.threadLock.release ()


    def RunThreadedQueues(self):
        try :
            t1 = threading.Thread ( target=self.AddtoQueue, args=(QueueList (), "Thread-1", 10000, 10000,) )
            t1.start()

            t2 = threading.Thread ( target=self.RemovefromQueue, args=(QueueList (), "Thread-2", 10000, 10000,) )
            t2.start()

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

    sr.RunThreadedQueues()
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




