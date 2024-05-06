
from matplotlib import pyplot as plt
import numpy as np
import random
import csv

from checker import Checker
from gate import Gate
from task import Task



class MonteCarloSimulation:

    def __init__(self, project, number_of_runs):
        self.project = project
        self.number_of_runs = number_of_runs

    def generate_workload(self):
        return random.random() #float between 0 and 1
 
    def calculate_actual_duration(self, min, exp, max):
        return random.triangular(min, exp, max)

    def calculate_durations(self):
        for lane in self.project.lanes.values():
            # print(lane.id)
            workload = self.generate_workload()
            lane.workload = workload
            # sette workload, bruk self.generate_workload(self) på lane
            for task in self.project.get_tasks():
                task.workload = workload
                #oppdatere task sin workload
                expected_duration = task.calculate_expected_duration()
                task.set_expected_duration(expected_duration)
                # set expected duration via func i task.py på alle tasks 
            
        for task in self.project.get_tasks():
            min = task.get_minimum_duration()
            exp = task.get_expected_duration()
            max = task.get_maximum_duration()
            actual_time = self.calculate_actual_duration(min, exp, max)
            task.set_actual_time(actual_time)
            # set actual time via self.calculate_actual_duration(min, exp, max)

    # Function to calculate times for project nodes
    def calculate_start_and_end_times_for_nodes(self):
        nodes = self.project.get_nodes().values()

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
                            actual_time = self.calculate_actual_duration(node.minimum_duration, node.expected_duration, node.maximum_duration)
                        elif isinstance(node, Gate):
                            actual_time = 0
                        # print(f"actual time for {node.id} is {actual_time}")
                        end_time = node.start_time + actual_time
                        node.set_end_time(end_time)
                        # print(f"end time for {node.id} is {end_time}\n")
        return self.project
    
    # Function to execute the Monte Carlo Simulation and write the results to a .csv-file.
    def execute_mc_simulation(self, csv_filename):
        with open(csv_filename, 'w', newline='') as csvfile:
            
            fieldnames = ['Run'] + [task.get_id() for task in self.project.get_tasks()] + ["Total duration at mid_gate", "Total duration"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            
            all_project_durations = {}
            for i in range(self.number_of_runs):
                self.calculate_durations()
                self.calculate_start_and_end_times_for_nodes()
                
                # Find mid gate
                mid_gate = None
                for gate in self.project.get_gates():
                    if gate.id == "MidProject":
                        mid_gate = gate
                
                # Find tasks up until the mid gate
                tasks_until_mid_gate = []
                for task in self.project.get_tasks():
                    if not task.get_end_time() > mid_gate.get_start_time():
                        tasks_until_mid_gate.append(task)
                
                # Find the duration until the mid gate
                total_mid_project_duration = 0
                for task in tasks_until_mid_gate:
                    total_mid_project_duration += task.get_actual_time()
                
                # Find the project total turation
                total_project_duration = 0 
                for task in self.project.get_tasks():
                    total_project_duration += task.get_actual_time()
            
                task_durations = {task.get_id(): round(task.get_actual_time(),1) for task in self.project.get_tasks()}
                
                all_project_durations[i+1] = total_project_duration

                #Write data to csv
                writer.writerow({'Run': i+1,
                                 **task_durations,
                                 "Total duration at mid_gate": round(total_mid_project_duration,4),
                                 "Total duration": round(total_project_duration,4)})
        return all_project_durations
            
    # Function to generate project statistics
    def project_statistics(self, durations):
        mean_duration = np.mean(durations)
        std_dev = np.std(durations)
        min_duration = np.min(durations)
        max_duration = np.max(durations)
        median = np.percentile(durations, 50)
        quantile_90 = np.percentile(durations, 90)
        
        return {
            "mean_duration": mean_duration,
            "std_dev": std_dev,
            "min_duration": min_duration,
            "max_duration": max_duration,
            "median": median,
            "quantile_90": quantile_90}

    # Function to plot histogram
    def plot_histogram(self, durations, bins=20):
        plt.hist(durations, bins=bins, alpha=0.7, color='b', edgecolor='black')
        plt.xlabel("Project Duration")
        plt.ylabel("Frequency")
        plt.title("Histogram of Project Durations")
        plt.show()



'''
decition tree
svm
lc
'''
