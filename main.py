from Stacks import StackLinkedList
from Stacks import StackList
from Queues import QueueLinkedList
from Queues import QueueList


if __name__ == '__main__' :

    stack = StackList ()

    print ( "Stack operations using LIST" )

    print ( "Push 4,5,6,7,8,10" )
    stack.push ( 4 )
    stack.push ( 5 )
    stack.push ( 6 )
    stack.push ( 7 )
    stack.push ( 8 )
    stack.push ( 10 )

    print(stack)

    p = stack.pop ()
    print("Pop {0}".format(p) )

    p = stack.pop ()
    print("Pop {0}".format(p) )

    print("Stack is now:")
    print(stack)

    stack = StackLinkedList ()

    print ( "Stack operations using  LinkedList" )
    print ("Push 4,5,6,7,8,10")
    stack.push ( 4 )
    stack.push ( 5 )
    stack.push ( 6 )
    stack.push ( 7 )
    stack.push ( 8 )
    stack.push ( 10 )

    print(stack)

    p = stack.pop ()
    print("Pop {0}".format(p) )

    p = stack.pop ()
    print("Pop {0}".format(p) )

    print ( "Stack is now:" )
    print ( stack )

    print ( "Queue operations using linked list" )
    queue = QueueLinkedList()

    print ( "Enqueue: 4,5,6,7,8,10" )
    queue.enqueue ( 4 )
    queue.enqueue ( 5 )
    queue.enqueue ( 6 )
    queue.enqueue ( 7 )
    queue.enqueue ( 8 )
    queue.enqueue ( 10 )
    print(queue)

    p = queue.dequeue ()
    print("Dequeued {0}".format(p))
    p = queue.dequeue ()
    print ( "Dequeued {0}".format ( p ) )
    print ( "After applying dequeue() two times" )
    print(queue)

    print("Queue List ----------------------------")

    print ( "Queue operations using list" )
    queue = QueueList()

    print ( "Enqueue: 4,5,6,7,8,10" )
    queue.enqueue ( 4 )
    queue.enqueue ( 5 )
    queue.enqueue ( 6 )
    queue.enqueue ( 7 )
    queue.enqueue ( 8 )
    queue.enqueue ( 10 )
    print(queue)

    p = queue.dequeue ()
    print("Dequeued {0}".format(p))
    p = queue.dequeue ()
    print ( "Dequeued {0}".format ( p ) )
    print ( "After applying dequeue() two times" )
    queue.printqueue ()

