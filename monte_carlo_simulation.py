
import random

from checker import Checker
from gate import Gate
from task import Task


class MonteCarloSimulation:

    def __init__(self):
        pass

    def generate_workload(self):
        return random.random() #float between 0 and 1
    
    """
    Må et sted lage workload, adde det til lane, og da også alle tasks i den lanen.
    """

    # We have the expected 
    def draw_pseudo_random_duration(self, min, max):
        return random.uniform(min, max)


    def calculate_start_and_end_times_for_nodes(self, project):
        nodes = project.get_nodes().values()

        while any(node.get_start_time() == -1 for node in nodes):
            for node in nodes:
                if node.get_start_time() == -1: #the node has not been updated.
                    in_constraints = node.get_in_constraints() #to find presuccessors in next line.
                    if all(con.source_node.get_start_time() != -1 for con in in_constraints): #all presuccessors have been updated
                        
                        #Set start time
                        if len(in_constraints) != 0: #we have presuccesors, not in start gate!
                            start_time = max(con.source_node.get_end_time() for con in in_constraints)
                            # max_node = next(con.source_node for con in in_constraints if con.source_node.end_time == start_time)
                            # print(f"end time for node {max_node.id} == start time for {node.id}: {start_time}")
                        else:
                            start_time = 0
                            # print(f"start time for {node.id}: {start_time}")
                        node.set_start_time(start_time)

                        #Set end time
                        if isinstance(node, Task):
                            actual_time = self.draw_pseudo_random_duration(node.minimum_duration, node.maximum_duration)
                        elif isinstance(node, Gate):
                            actual_time = 0 #TODO-QUESTION: WHAT??
                        # print(f"actual time for {node.id} is {actual_time}")
                        end_time = node.start_time + actual_time
                        node.set_end_time(end_time)
                        # print(f"end time for {node.id} is {end_time}\n")
        return project

    # def calculate_times_for_all_nodes(self, project):
    #     # for node in project.nodes.values():
    #     # finne den første noden.
    #     start_node = Checker.check_start_node(project)
    #     start_node.set_start_time(0)
    #     #TODO: QUESTION: Gate har ikke min og max, hva skal actual tid være, 0??
    #     start_node.set_end_time(start_node.start_time) #+ start_node.actual_time)

    #     self.calculate_for_next(start_node)


    # def calculate_for_next_nodes(self, prev_node):
    #     out_constraints = prev_node.get_out_constraints()

    #     target_nodes = []
    #     for constraint in out_constraints:
    #         #source node til constraint er startnoden
    #         target_nodes.append(constraint.target_node)

    #     for node in target_nodes:
    #         self.calculate_for_next_node(prev_node, node)
        

    # def calculate_for_next_node(self, prev_node, node):
    #     node.set_start_time(prev_node.end_time)
    #     node.set_end_time(node.start_time + node.actual_time)