
class Node:

    def __init__(self, id): #in_constraints, out_constraints):
        self.id = id
        self.in_constraints = [] #in_constraints
        self.out_constraints = []
        self.start_time = None  #start tid er gitt fra forrige node sin egen tid
        self.end_time = None    # end time er gitt start tid + faktisk (actual) tid.
                                # End tid for denne er start tid for neste node.
        self.actual_time = None # tid som kommer fra simulasjonene som blir kjørt. 

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