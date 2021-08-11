from StackLinkedList import StackLinkedList


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
