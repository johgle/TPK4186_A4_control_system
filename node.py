
class Node:

    def __init__(self, id): #in_constraints, out_constraints):
        self.id = id
        self.in_constraints = []
        self.out_constraints = []
        self.start_time = -1  #start_time is from the former node's end_time. If start_gate it is 0.
        self.end_time = -1    # end_time is start_time + actual_time
        self.actual_time = None # actual_time is None until the simulations is run and it is updated with real data.

    def get_id(self):
        return self.id
    
    def set_id(self, new_id):
        self.id = new_id

    def get_in_constraints(self):
        return self.in_constraints
    
    def set_in_constraints(self, in_constraints):
        self.in_constraints = in_constraints

    def add_in_constraints(self, in_constraint):
        self.in_constraints.append(in_constraint)
    
    def get_out_constraints(self):
        return self.out_constraints
    
    def set_out_constraints(self, out_constraints):
        self.out_constraints = out_constraints

    def add_out_constraints(self, out_constraint):
        self.out_constraints.append(out_constraint)

    def get_start_time(self):
        return self.start_time
    
    def set_start_time(self, time):
        self.start_time = time

    def get_end_time(self):
        return self.end_time
    
    def set_end_time(self, time):
        self.end_time = time

    def get_actual_time(self):
        return self.actual_time
    
    def set_actual_time(self, time):
        self.actual_time = time