
from node import Node

class Task(Node):

    def __init__(self, id, minimum_duration, maximum_duration):
        Node.__init__(self, id)
        self.minimum_duration = minimum_duration
        self.maximum_duration = maximum_duration
        self.expected_duration = 0 #mode
        self.workload = 0
        self.lane = None

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

    def get_workload(self):
        return self.workload
    
    def set_workload(self, workload):
        self.workload = workload

    def get_lane(self):
        return self.get_lane
    
    def set_lane(self, lane):
        self.lane = lane

    def calculate_expected_duration(self):
        return self.minimum_duration + (self.maximum_duration - self.minimum_duration)*self.workload
        