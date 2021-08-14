
from Nodes import Node

class BaseQueue:
    def enqueue(self, data) :
        pass

    def dequeue(self) :
        pass

    def isEmpty(self) :
        pass

    def __str__(self):
        pass

class QueueList(BaseQueue):

    def __init__(self) :
        self.queuelist = []

    def enqueue(self, data) :
        n = Node ( data )
        self.queuelist.append(n)

    def dequeue(self) :
        if self.isEmpty():
            return None
        r = self.queuelist.pop(0)
        return r.data

    def isEmpty(self) :
        r = False
        if len ( self.queuelist ) == 0 :
            r = True
        return r

    def __str__(self):
        r = ""
        for q in reversed(self.queuelist):
            r += str( q.data ) + " -> "
        return r


class QueueLinkedList(BaseQueue) :

    def __init__(self) :
        self.front = self.rear = None

    def isEmpty(self) :
        return self.front == None

    def enqueue(self, item) :
        temp = Node ( item )

        if self.rear == None :
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self) :
        if self.isEmpty () :
            return None
        temp = self.front
        self.front = temp.next

        if (self.front == None) :
            self.rear = None
        return temp.data

    def __str__(self):
        r = ""
        s = self.front
        while s != None:
            r = (str(s.data) + " -> ") + r
            s = s.next
        return r




