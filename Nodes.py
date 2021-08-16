

class BaseNode :
    def __init__(self, data):
        self.data = data

class Node :
    def __init__(self, data) :
        self.data = data  # Assign data
        self.next = None
        BaseNode.__init__ ( self, data )
