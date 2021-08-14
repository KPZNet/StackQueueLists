
from Nodes import Node

class BaseQueue:
    def enqueue(self, data) :
        pass

    def dequeue(self) :
        pass

    def first(self) :
        pass

    def size(self) :
        pass

    def isEmpty(self) :
        pass

    def printqueue(self) :
        pass


class QueueList(BaseQueue):

    def __init__(self) :
        self.queuelist = []

    def enqueue(self, data) :
        n = Node ( data )
        self.queuelist.append(n)

    def dequeue(self) :
        r = self.queuelist.pop()
        return r.data

    def first(self) :
        f = None
        if not self.isEmpty():
            f = self.queuelist[0]
        return f

    def size(self) :
        s = 0
        if not self.isEmpty():
            s = len ( self.queuelist )
        return s

    def isEmpty(self) :
        r = False
        if len ( self.queuelist ) == 0 :
            r = True
        return r

    def __str__(self):
        r = ""
        for q in self.queuelist:
            r += str( q.data ) + " : "
        return r



# A class to represent a queue
class QueueLinkedList(BaseQueue) :

    def __init__(self) :
        self.front = self.rear = None

    def isEmpty(self) :
        return self.front == None

    # Method to add an item to the queue
    def enqueue(self, item) :
        temp = Node ( item )

        if self.rear == None :
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def dequeue(self) :

        if self.isEmpty () :
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None) :
            self.rear = None
        return temp.data

    def __str__(self):
        r = ""
        s = self.front
        while s != None:
            r += (str(s.data) + " : ")
            s = s.next
        return r




