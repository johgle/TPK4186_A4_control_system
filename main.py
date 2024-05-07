

'''
File Overview:
Resources, Required Modules
1. Functions
2. For tester (Want to test? Search for TODO to find it easily)
3. main function

'''

# Resorces
# ------------
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/xml.dom.minidom.html
# https://scikit-learn.org/stable/index.html

# Required Modules
# -------------------
import sys
import numpy
from checker import Checker
from monte_carlo_simulation import MonteCarloSimulation
from project_parser import ProjectParser
from classifier import *
from regressor import *

# 1.2 For Classifier:
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import NearestCentroid

# 1.3 For Regression:
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR


# Instances
# --------------------
parser = ProjectParser()

# 1. Functions
# --------------------

# Parse project and save in an object
max_durations = [115, 117, 120]
# project = parser.parse_project("ControlSystemProject.xml")
# mcs = MonteCarloSimulation(project, 1000)


# # CLASSIFIER
# for max_duration in max_durations:
#     all_project_durations = mcs.execute_mc_simulation("ControlSystemProject_simulations.csv", max_duration)
#     mcs.split_result_into_test_and_training("ControlSystemProject_simulations.csv")

#     project_duration_list = list(all_project_durations.values())

#     # Compute statistics
#     stats = mcs.calculate_project_statistics(project_duration_list)
#     print("Project Statistics:", stats, "\n")

#     # Plot histogram
#     mcs.plot_histogram(project_duration_list)

#     # 3. Loading of training and test sets
#     # ------------------------------------
#     training_set = numpy.genfromtxt("training_set_classification.csv", delimiter=',')
#     training_instances = training_set[1:, 0:-3]
#     training_labels = training_set[1:, -1]

#     test_set = numpy.genfromtxt("test_set_classification.csv", delimiter=',')
#     test_instances = test_set[1:, 0:-3]
#     test_labels = test_set[1:, -1]


#     # 4. Classification
#     # -------------------

#     model_svc = SVC()
#     model_svc.fit(training_instances, training_labels)
#     predicted_labels = model_svc.predict(test_instances)
#     export_confusion_matrix(["on-time", "delayed"], test_labels, predicted_labels, "ResultsClassification.csv", "SVC", max_duration)

#     model_dtc = DecisionTreeClassifier()
#     model_dtc.fit(training_instances, training_labels)
#     predicted_labels = model_dtc.predict(test_instances)
#     export_confusion_matrix(["on-time", "delayed"], test_labels, predicted_labels, "ResultsClassification.csv", "Decision Tree Classifier", max_duration)

#     model_mlpc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
#     model_mlpc.fit(training_instances, training_labels)
#     predicted_labels = model_mlpc.predict(test_instances)
#     export_confusion_matrix(["on-time", "delayed"], test_labels, predicted_labels, "ResultsClassification.csv", "MLPClassifier", max_duration)

#     model_nc = NearestCentroid()
#     model_nc.fit(training_instances, training_labels)
#     predicted_labels = model_nc.predict(test_instances)
#     export_confusion_matrix(["on-time", "delayed"], test_labels, predicted_labels, "ResultsClassification.csv", "Nearest Centroid", max_duration)

# # REGRESSION:

# # 3. Loading of training and test sets
# training_set = numpy.genfromtxt("training_set_classification.csv", delimiter=',')
# training_instances = training_set[1:, 0:-3]
# training_labels = training_set[1:, -1]

# test_set = numpy.genfromtxt("test_set_classification.csv", delimiter=',')
# test_instances = test_set[1:, 0:-3]
# test_labels = test_set[1:, -1]


# Regression:
# --------------------------

# model_svr = SVR()
# model_svr.fit(training_instances, training_labels)
# predicted_labels = model_svr.predict(test_instances)
# # print_results(test_labels, predicted_labels, sys.stdout)
# export_results(test_labels, predicted_labels, "results_regression.csv")

# model_mlpr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 5, 2), random_state=1)
# model_mlpr.fit(training_instances, training_labels)
# predicted_labels = model_mlpr.predict(test_instances)
# # print_results(test_labels, predicted_labels, sys.stdout)
# export_results(test_labels, predicted_labels, "results_regression.csv")

# model_lr = LogisticRegression(random_state=1)
# model_lr.fit(training_instances, training_labels)
# predicted_labels = model_lr.predict(test_instances)
# # print_results(test_labels, predicted_labels, sys.stdout)
# export_results(test_labels, predicted_labels, "results_regression.csv")



def read_a_project_successfully_to_the_program(): #1
    return parser.parse_project("ControlSystemProject.xml")

def print_project_to_terminal(): #2
    parser.print_project(read_a_project_successfully_to_the_program())

def check_whether_a_project_is_correctly_designed(): #3
    checker = Checker()
    project = parser.parse_project("ControlSystemProject.xml")
    start = checker.check_start_node(project)[0]
    end = checker.check_end_node(project)[0]
    print("The project is now checked:\n"+
          f"Only one start node, and it's a gate: {start}.\n"+
          f"Only one end node, and it's a gate: {end}.")
    
def filenamecalculate_stats_and_plot_histogram_using_mcs_results(): #4
    # Add project to program
    project = parser.parse_project("ControlSystemProject.xml")
    
    # Run MCSimulation and extract duration of all projects
    mcs = MonteCarloSimulation(project, 1000)
    all_project_durations = mcs.execute_mc_simulation("ControlSystemProject_simulations.csv", 0) # max_duration = 0 because it has nothing to say for this task!
    project_duration_list = list(all_project_durations.values())

    # Compute statistics
    stats = mcs.calculate_project_statistics(project_duration_list)
    print("Project Statistics:", stats, "\n")

    # Plot histogram
    mcs.plot_histogram(project_duration_list)


# 2. For tester
# --------------------
"""

FOR TESTER:
    To make it easy to test the differnt functions of the program, you can choose between which
    function to test next by changing the value for "TASK_TO_TEST".
    
    Choose the value from 1-6 for TASK_TO_TEST to execute your wanted test:
    1 - Read a project successfully to the program
    2 - Print a project to terminal
    3 - Check whether a project is correctly designed
    4 - Calculate stats and plot histogram for results of Monte Carlo Simulations
    5 - Predict project durations using classification-algorithms
    6 - Predict project durations using regression-algorithms
    Note: Every other number is not allowed and will print out an error-message to the terminal
"""

#TODO: CHANGE VALUE HERE, [1-6]:
TASK_TO_TEST = 4

# 3. main function
# --------------------

if __name__ == '__main__':
    #  Read a project successfully to the program:
    if TASK_TO_TEST == 1:
        read_a_project_successfully_to_the_program()
    
    # Print a project to terminal
    elif TASK_TO_TEST == 2:
        print_project_to_terminal()

    # Check whether a project is correctly designed
    elif TASK_TO_TEST == 3:
        check_whether_a_project_is_correctly_designed()

    # Calculate stats and plot histogram for results of Monte Carlo Simulations
    elif TASK_TO_TEST == 4:
        filenamecalculate_stats_and_plot_histogram_using_mcs_results()

    # Predict project durations using classification-algorithms
    elif TASK_TO_TEST == 5:
        predict_using_classification()

    # Predict project durations using regression-algorithms
    elif TASK_TO_TEST == 6:
        predict_using_regression()

    else:
        print(f"Error: You have given the number {TASK_TO_TEST}, which is not allowed. Please specify which test you want to execute by using a number between 1 and 6.")