# Machine Learning - Introduction
# Classifier.py
# by Antoine Rauzy
# Copyrights (c) 2022 NTNU
# NOTE: Changed by Johanne Glende to fit assignment 4 spring 2024.

# 1. Required Modules
# -------------------
from sklearn.metrics import accuracy_score

# 2. Functions to print results as matrixes
# -----------------------------------------

def export_confusion_matrix(labels, actual_labels, predicted_labels, filename, algorithm_id, max_duration):
    output = open(filename, mode="a") # a (append) so that we get data from multiple algorithms in one file
    print_confusion_matrix(labels, actual_labels, predicted_labels, output, algorithm_id, max_duration)
    output.close()

def print_confusion_matrix(labels, actual_labels, predicted_labels, output, algorithm_id, max_duration):
    output.write(f"{algorithm_id.upper()}. Max duration: {max_duration}\n")
    
    accuracy = accuracy_score(actual_labels, predicted_labels)
    output.write(f"Accuracy {algorithm_id}: {accuracy}\n")
    
    number_of_labels = len(labels)
    counts = [[0 for _ in range(0, number_of_labels)] for _ in range(0, number_of_labels)]
    for i in range(0, len(actual_labels)):
        counts[int(actual_labels[i])][int(predicted_labels[i])] += 1
    output.write("\t\t\t\tPredicted \n\t\t\t")
    for column in range(0, number_of_labels):
        output.write("\t{0:s}".format(labels[column]))
    output.write("\n")
    for row in range(0, number_of_labels):
        output.write("Actual {0:s}\t\t".format(labels[row]))
        for column in range(0, number_of_labels):
            output.write("{0:d}\t\t".format(counts[row][column]))
        output.write("\n")
    output.write("\n-------------------------------------------------------\n\n")
