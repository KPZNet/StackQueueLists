

class BaseNode :
    def __init__(self, value):
        self.value = value

class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None
        self.prev = None
        BaseNode.__init__ ( self, value )

# Node class
class NodeQueue :

    # Function to initialise the node object
    def __init__(self, data) :
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null