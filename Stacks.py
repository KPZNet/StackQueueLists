from Nodes import Node

class BaseStack:
    def push(self, node):
        pass

    def pop(self):
        pass

    def isEmpty(self) :
        pass

    def __str__(self) :
        pass


class StackList(BaseStack):
    def __init__(self) :
        self.stk = []

    def isEmpty(self):
       if self.stk==[]:
          return True
       else:
          return False

    def push(self,item):
       self.stk.append(item)
       top=len(self.stk)-1

    def pop(self):
        r = None
        if self.isEmpty():
          print("Underflow")
        else:
          r =self.stk.pop()
        return r

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
    def __init__(self) :
        self.head = Node ( "head" )
        self.size = 0

    def __str__(self) :
        cur = self.head.next
        out = ""
        while cur :
            out += str ( cur.data ) + "\n"
            cur = cur.next
        return out

    def isEmpty(self) :
        return self.size == 0

    def push(self, value) :
        node = Node ( value )
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self) :
        if self.isEmpty () :
            raise Exception ( "Popping from an empty stack" )
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data





