
from Nodes import Node

class BaseQueue:
    def enqueue(self, data) :
        pass

    def dequeue(self) :
        pass

class QueueList(BaseQueue):

    def __init__(self) :
        self.queuelist = []

    def enqueue(self, data) :
        n = Node ( data )
        self.queuelist.append(n)

    def dequeue(self) :
        return self.queuelist.pop()

    def first(self) :
        f = None
        if not self.isEmpty():
            f = self.queuelist[0]
        return f

    def size(self) :
        s = 0
        if not self.isEmpty():
            s = len ( self.queuelist )
        else:
            s = 0
        return s

    def isEmpty(self) :
        if len ( self.queuelist ) == 0 :
            return True
        else :
            return False

    def printqueue(self) :
        print ( "queue elements are:" )
        for q in self.queuelist:
            print ( q.data, end="->" )




class QueueLinkedList (BaseQueue) :

    def __init__(self) :
        self.head = None
        self.last = None

    def enqueue(self, data) :
        if self.last is None :
            self.head = Node ( data )
            self.last = self.head
        else :
            self.last.next = Node ( data )
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self) :
        if self.head is None :
            return None
        else :
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self) :
        return self.head.data

    def size(self) :
        temp = self.head
        count = 0
        while temp is not None :
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self) :
        if self.head is None :
            return True
        else :
            return False

    def printqueue(self) :
        print ( "queue elements are:" )
        temp = self.head
        while temp is not None :
            print ( temp.data, end="->" )
            temp = temp.next

