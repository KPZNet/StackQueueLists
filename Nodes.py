

class BaseNode :
    def __init__(self, value):
        self.value = value

class Node :
    def __init__(self, value) :
        self.value = value
        self.data = value  # Assign data
        self.next = None
        self.prev = None
        BaseNode.__init__ ( self, value )
