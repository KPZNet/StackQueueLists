from Stacks import StackLinkedList
from Stacks import StackList
from Queues import QueueLinkedList
from Queues import QueueList
import time

NANO_TO_MS = 1000000

class StackRunner:
    def __init__(self):
        self.ls = StackList()
        self.lls = StackLinkedList()
        self.ls_timing = 0.0
        self.lls_timing = 0.0

    def RunQueueList(self, runs, size, qu):
        print("<<< Queue List RunTimes >>>")
        ll = qu

        start_time = time.perf_counter_ns ()

        for k in range(runs):
            for i in range ( size ) :
                ll.enqueue ( i )

            for j in range ( size ) :
                ll.dequeue ()

            if not ll.isEmpty():
                print("ERROR QUEUE NOT EMPTY")

        stop_time = time.perf_counter_ns ()
        self.ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  self.ls_timing

    def RunQueueList2(self, runs, size, qu):
        print("<<< Queue List RunTimes >>>")
        ll = qu

        start_time = time.perf_counter_ns ()

        for k in range(runs):
            for i in range ( size/4 ) :
                ll.enqueue ( i )

            for j in range ( size ) :
                ll.dequeue ()

            if not ll.isEmpty():
                print("ERROR QUEUE NOT EMPTY")

        stop_time = time.perf_counter_ns ()
        self.ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  self.ls_timing




if __name__ == '__main__' :

    sr = StackRunner()
    lq_time = sr.RunQueueList(1000, 2, QueueList())
    llq_time = sr.RunQueueList ( 10000, 2, QueueLinkedList () )
    print ( "List Type:{0}  vs. LinkedList Type{1}".format(lq_time, llq_time) )

    lq_time = sr.RunQueueList(2, 10000, QueueList())
    llq_time = sr.RunQueueList ( 2, 10000, QueueLinkedList () )
    print ( "List Type:{0}  vs. LinkedList Type{1}".format(lq_time, llq_time) )




