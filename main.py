from Stacks import StackLinkedList
from Stacks import StackList
from Queues import QueueLinkedList
from Queues import QueueList


class StackRunner:
    def __init__(self):
        self.ls = StackList()
        self.lls = StackLinkedList()
        self.ls_timing = 0.0
        self.lls_timing = 0.0

    def RunQueueList(self, runs, qu):
        print("Queue List")
        ll = qu
        print("Enqueing 5-6-2-10")
        ll.enqueue ( 5 )
        ll.enqueue ( 6 )
        ll.enqueue ( 2 )
        ll.enqueue ( 10 )
        print(ll)

        dq = ll.dequeue()
        print(dq)






if __name__ == '__main__' :

    sr = StackRunner()
    sr.RunQueueList(10, QueueList())
    sr.RunQueueList ( 10, QueueLinkedList () )




