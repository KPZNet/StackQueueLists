from StackLinkedList import StackLinkedList
from QueueLinkedList import QueueLinkedList


if __name__ == '__main__' :


    stack = StackLinkedList ()

    print ( "Stack operations using Doubly LinkedList" )
    stack.push ( 4 )
    stack.push ( 5 )
    stack.push ( 6 )
    stack.push ( 7 )

    stack.printstack ()

    print ( "\nTop element is ", stack.top () )
    print ( "Size of the stack is ", stack.size () )


    stack.pop ()
    stack.pop ()
    stack.printstack ()

    print ( "\nstack is empty:", stack.isEmpty () )

    queue = QueueLinkedList()

    print ( "Queue operations using doubly linked list" )

    queue.enqueue ( 4 )
    queue.enqueue ( 5 )
    queue.enqueue ( 6 )
    queue.enqueue ( 7 )
    queue.printqueue ()

    print ( "\nfirst element is ", queue.first () )
    print ( "Size of the queue is ", queue.size () )
    queue.dequeue ()
    queue.dequeue ()
    print ( "After applying dequeue() two times" )
    queue.printqueue ()

    print ( "\nqueue is empty:", queue.isEmpty () )

