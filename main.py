from Stacks import StackLinkedList
from Queues import QueueLinkedList
from Queues import QueueList



if __name__ == '__main__' :

    stack = StackLinkedList ()

    print ( "Stack operations using  LinkedList" )
    stack.push ( 4 )
    stack.push ( 5 )
    stack.push ( 6 )
    stack.push ( 7 )
    stack.push ( 8 )
    stack.push ( 10 )

    print(stack)

    stack.pop ()
    stack.pop ()
    print(stack)

    print ( "Queue operations using doubly linked list" )
    queue = QueueLinkedList()

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

    print("Queue List ----------------------------")

    print ( "Queue operations using list" )
    queue = QueueList()

    queue.enqueue ( 4 )
    queue.enqueue ( 5 )
    queue.enqueue ( 6 )
    queue.enqueue ( 7 )
    queue.printqueue ()

    print ( "\nfirst element is ", queue.first ().data )
    print ( "Size of the queue is ", queue.size () )
    queue.dequeue ()
    queue.dequeue ()
    print ( "After applying dequeue() two times" )
    queue.printqueue ()

    print ( "\nqueue is empty:", queue.isEmpty () )

    print("Queue TEST for List")
    q = QueueList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    d = q.dequeue()
    print(d.data)