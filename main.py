from StackLinkedList import StackLinkedList
from QueueLinkedList import QueueLinkedList

# Code execution starts here
if __name__ == '__main__' :

    # Start with the empty stack
    stack = StackLinkedList ()

    # Insert 4 at the beginning. So stack becomes 4->None
    print ( "Stack operations using Doubly LinkedList" )
    stack.push ( 4 )

    # Insert 5 at the beginning. So stack becomes 4->5->None
    stack.push ( 5 )

    # Insert 6 at the beginning. So stack becomes 4->5->6->None
    stack.push ( 6 )

    # Insert 7 at the beginning. So stack becomes 4->5->6->7->None
    stack.push ( 7 )

    # Print the stack
    stack.printstack ()

    # Print the top element
    print ( "\nTop element is ", stack.top () )

    # Print the stack size
    print ( "Size of the stack is ", stack.size () )

    # pop the top element
    stack.pop ()

    # pop the top element
    stack.pop ()

    # two elements are popped
    # Print the stack
    stack.printstack ()

    # Print True if the stack is empty else False
    print ( "\nstack is empty:", stack.isEmpty () )

    # This code is added by Suparna Raut

    # Start with the empty queue
    queue = QueueLinkedList()

    print ( "Queue operations using doubly linked list" )

    # Insert 4 at the end. So queue becomes 4->None
    queue.enqueue ( 4 )

    # Insert 5 at the end. So queue becomes 4->5None
    queue.enqueue ( 5 )

    # Insert 6 at the end. So queue becomes 4->5->6->None
    queue.enqueue ( 6 )

    # Insert 7 at the end. So queue becomes 4->5->6->7->None
    queue.enqueue ( 7 )

    # Print the queue
    queue.printqueue ()

    # Print the first element
    print ( "\nfirst element is ", queue.first () )

    # Print the queue size
    print ( "Size of the queue is ", queue.size () )

    # remove the first element
    queue.dequeue ()

    # remove the first element
    queue.dequeue ()

    # first two elements are removed
    # Print the queue
    print ( "After applying dequeue() two times" )
    queue.printqueue ()

    # Print True if queue is empty else False
    print ( "\nqueue is empty:", queue.isEmpty () )

