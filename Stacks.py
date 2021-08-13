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


class StackList:
    def __init__(self) :
        self.head = Node ( "head" )
        self.size = 0

    def isEmpty(stk): # checks whether the stack is empty or not
       if stk==[]:
          return True
       else:
          return False

    def Push(stk,item): # Allow additions to the stack
       stk.append(item)
       top=len(stk)-1

    def Pop(stk):
       if isEmpty(stk): # verifies whether the stack is empty or not
          print("Underflow")
       else: # Allow deletions from the stack
          item=stk.pop()
          if len(stk)==0:
             top=None
          else:
             top=len(stk)
             print("Popped item is "+str(item))

    def Display(stk):
       if isEmpty(stk):
          print("Stack is empty")
       else:
          top=len(stk)-1
          print("Elements in the stack are: ")
          for i in range(top,-1,-1):
             print (str(stk[i]))




class StackLinkedList (BaseStack) :
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self) :
        self.head = Node ( "head" )
        self.size = 0

    def printstack(self):
        self.__str__()

    # String representation of the stack
    def __str__(self) :
        cur = self.head.next
        out = ""
        while cur :
            out += str ( cur.data ) + "->"
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





