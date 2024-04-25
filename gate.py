# Node is a superclass. Gate is a specific type of Node.
from node import Node

class Gate(Node):

    def __init__(self, id):
        Node.__init__(self, id)