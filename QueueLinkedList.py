# A complete working Python program to demonstrate all
# Queue operations using doubly linked list

# Node class
class NodeQueue :

    # Function to initialise the node object
    def __init__(self, data) :
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null



class QueueLinkedList :

    def __init__(self) :
        self.head = None
        self.last = None

    def enqueue(self, data) :
        if self.last is None :
            self.head = NodeQueue ( data )
            self.last = self.head
        else :
            self.last.next = NodeQueue ( data )
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

