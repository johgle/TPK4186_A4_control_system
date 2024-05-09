
# Table of Contents
# -----------------
# 1. Imported modules
# 2. Parser

# 1. Imported modules
# -----------------
import re
import xml.dom.minidom #dom means document
from gate import Gate
from monte_carlo_simulation import MonteCarloSimulation
from project import Project
from checker import Checker


# 2. Parser
# -----------------

class ProjectParser():

    def __init__(self):
        pass

    def parse_project(self, filename):
        document = xml.dom.minidom.parse(filename)
        project = self.read_project(document)
        print(f"The project, {project.id}, from the file, {filename}, was read successfully to the program.\n")
        return project
    
    def read_project(self, input_file):
        project = Project(input_file.getElementsByTagName("project")[0].getAttribute("name"))

        # Add gates to project
        gates = input_file.getElementsByTagName("gate")
        for i in gates:
            project.new_gate(i.getAttribute("name"))

        #Add lanes with their tasks to project
        lanes = input_file.getElementsByTagName("lane")
        for l in lanes:
            new_lane = project.new_lane(l.getAttribute("name"))

            tasks = l.getElementsByTagName("task")
            for t in tasks: 
                new_task = project.new_task(t.getAttribute("name"), float(t.getAttribute("minimum-duration")), float(t.getAttribute("maximum-duration")))
                new_task.set_lane(new_lane)
                new_lane.append_task(new_task)
            
        #Add constraints to project
        constraints = input_file.getElementsByTagName("precedence-constraint")
        for c in constraints:
            source_node = project.look_for_node(c.getAttribute("source"))
            target_node = project.look_for_node(c.getAttribute("target"))

            new_constraint = project.new_constraint(source_node, target_node)
            source_node.add_out_constraints(new_constraint)
            target_node.add_in_constraints(new_constraint)

        return project

    def print_project(self, project):
        print("Project", project.id)
        self.print_gates(project)
        self.print_lanes(project)
        self.print_constraints(project)
        print("end")

    def print_gates(self, project):
        for g in project.nodes.values():
            if isinstance(g, Gate):
                self.print_gate(g)

    def print_gate(self, gate):
        print("\tGate", gate.id)

    def print_lanes(self, project):
        for lane in project.lanes.values():
            self.print_lane(lane)

    def print_lane(self, lane):
        print("\tLane", lane.id, lane.workload)
        self.print_tasks(lane)

    def print_tasks(self, lane):
        for task in lane.tasks:
            self.print_task(task)

    def print_task(self, task):
        print("\t\tTask", task.id, task.minimum_duration, task.maximum_duration, task.expected_duration)

    def print_constraints(self, project):
        for constraint in project.constraints:
            self.print_constraint(constraint)
    
    def print_constraint(self, constraint):
        print("\tConstraint", constraint.source_node.id, "-", constraint.target_node.id)

