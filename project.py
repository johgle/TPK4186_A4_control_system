
from gate import Gate
from lane import Lane
from task import Task
from precedence_constraints import Constraint


class Project:

    def __init__(self, id):
        self.id = id
        self.nodes = {}
        self.lanes = {}
        self.constraints = []
        """ From Prof: We use dictionaries for when we have things that needs to be sorted and have they have a specific identifier."""

    def get_id(self):
        return self.id
    
    def set_id(self, new_id):
        self.id = new_id

    def get_nodes(self):
        return self.nodes
    
    def new_gate(self, id):
        gate = Gate(id)
        self.nodes[id] = gate
        return gate
      
    def new_task(self, id, min_dur, max_dur):
        task = Task(id, min_dur, max_dur)
        self.nodes[id] = task
        return task
    
    def look_for_node(self, node_id):
        return self.nodes.get(node_id, None)
    
    def get_contraints(self):
        return self.constraints
    
    def new_constraint(self, source, target):
        constraint = Constraint(source, target)
        self.constraints.append(constraint)
        return constraint
    
    def get_lanes(self):
        return self.lanes.values()
    
    def look_for_lane(self, lane_id):
        return self.lanes.get(lane_id, None)

    def new_lane(self, id):
        lane = Lane(id)
        self.lanes[id] = lane
        # print("Lane added")
        return lane

    def print_nodes(self):
        for key, value in self.nodes.items():
            if isinstance(value, Gate):
                print(key+":"+ str(value))
            if isinstance(value, Task):
                print(key+":",value.id, value.minimum_duration, value.maximum_duration, value.expected_duration)

    def print_constraints(self):
        for c in self.constraints:
            print("Constraint", c.source_node.id, "-", c.target_node.id)