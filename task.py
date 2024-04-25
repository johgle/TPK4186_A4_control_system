
from node import Node

#For task we use triangular distributions. Between minimum and maximum on x-axis, and a top "mode" on y-axis.

class Task(Node):

    def __init__(self, id):
        Node.__init__(self, id)
        self.minimum_duration = 0
        self.maximum_duration = 0
        self.expected_duration = 0 #mode

    def get_minimum_duration(self):
        return self.minimum_duration
    
    def set_minimum_duration(self, new_min_dur):
        self.minimum_duration = new_min_dur

    def get_maximum_duration(self):
        return self.maximum_duration
    
    def set_maximum_duration(self, new_max_dur):
        self.maximum_duration = new_max_dur

    def get_expected_duration(self):
        return self.expected_duration
    
    def set_expected_duration(self, new_exp_dur):
        self.expected_duration = new_exp_dur
