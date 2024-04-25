
class Constraint:

    def __init__(self, source_node, target_node):
        self.source_node = source_node
        self.target_node = target_node

    def get_target_node(self):
        return self.target_node
    
    def set_target_node(self, node):
        self.target_node = node
    
    def get_source_node(self):
        return self.source_node
    
    def set_source_node(self, node):
        self.source_node = node

