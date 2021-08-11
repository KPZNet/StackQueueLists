# A complete working Python program to demonstrate all
# stack operations using a doubly linked list


# Node class
class NodeStack :

    # Function to initialise the node object
    def __init__(self, data) :
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


# Stack class contains a Node object
class StackLinkedList :
    # Function to initialize head
    def __init__(self) :
        self.head = None

    # Function to add an element data in the stack
    def push(self, data) :

        if self.head is None :
            self.head = NodeStack ( data )
        else :
            new_node = NodeStack ( data )
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    # Function to pop top element and return the element from the stack
    def pop(self) :

        if self.head is None :
            return None
        elif self.head.next is None :
            temp = self.head.data
            self.head = None
            return temp
        else :
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    # Function to return top element in the stack
    def top(self) :

        return self.head.data

    # Function to return the size of the stack
    def size(self) :

        temp = self.head
        count = 0
        while temp is not None :
            count = count + 1
            temp = temp.next
        return count

    # Function to check if the stack is empty or not
    def isEmpty(self) :

        if self.head is None :
            return True
        else :
            return False

    # Function to print the stack
    def printstack(self) :

        print ( "stack elements are:" )
        temp = self.head
        while temp is not None :
            print ( temp.data, end="->" )
            temp = temp.next
