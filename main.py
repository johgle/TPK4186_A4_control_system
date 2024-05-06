

'''
Resorces:
https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/xml.dom.minidom.html

'''


from checker import Checker
from monte_carlo_simulation import MonteCarloSimulation
from project_parser import ProjectParser


parser = ProjectParser()
# checker = Checker()

# Parse project and save in an object
project = parser.parse_project("ControlSystemProject.xml")
mcs = MonteCarloSimulation(project, 50)
all_project_durations = mcs.execute_mc_simulation("ControlSystemProject_simulations.csv") #dict containing dicts!

project_duration_list = list(all_project_durations.values())
# for run, project_duration in all_project_durations.items():
#     project_duration_list.append(project_duration)


# Compute statistics
stats = mcs.project_statistics(project_duration_list)
print("Project Statistics:", stats)

# Plot histogram
mcs.plot_histogram(project_duration_list)

# if __name__ == '__main__':
#     pass