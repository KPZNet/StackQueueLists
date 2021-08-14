from Nodes import Node

# A complete working Python program to demonstrate all
# stack operations using a doubly linked list

class BaseStack:
    def push(self, node):
        pass

    def pop(self):
        pass

    def peek(self) :
        pass

    def printstack(self) :
        pass

    def getSize(self) :
        pass

    def isEmpty(self) :
        pass

    def __str__(self) :
        pass


class StackList(BaseStack):
    def __init__(self) :
        self.stk = []

    def isEmpty(self): # checks whether the stack is empty or not
       if self.stk==[]:
          return True
       else:
          return False

    def push(self,item): # Allow additions to the stack
       self.stk.append(item)
       top=len(self.stk)-1

    def pop(self):
        r = None
        if self.isEmpty(): # verifies whether the stack is empty or not
          print("Underflow")
        else: # Allow deletions from the stack
          r =self.stk.pop()
        return r


    def printstack(self):
        print(self)

    # String representation of the stack
    def __str__(self) :
        ret = ""
        if self.isEmpty ( ) :
            ret = "Stack Empty"
        else :
            top = len ( self.stk ) - 1
            for i in range ( top, -1, -1 ) :
                ret +=( ( str ( self.stk[i] ) ) + "\n")
        return ret

class StackLinkedList (BaseStack) :
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self) :
        self.head = Node ( "head" )
        self.size = 0

    def printstack(self):
        print(self)

    # String representation of the stack
    def __str__(self) :
        cur = self.head.next
        out = ""
        while cur :
            out += str ( cur.data ) + "\n"
            cur = cur.next
        return out

    # Get the current size of the stack
    def getSize(self) :
        return self.size

    # Check if the stack is empty
    def isEmpty(self) :
        return self.size == 0

    # Get the top item of the stack
    def peek(self) :
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty () :
            raise Exception ( "Peeking from an empty stack" )
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value) :
        node = Node ( value )
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self) :
        if self.isEmpty () :
            raise Exception ( "Popping from an empty stack" )
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data





