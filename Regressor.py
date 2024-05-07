# Machine Learning - Introduction
# Regressor.py
# by Antoine Rauzy
# Copyrights (c) 2022 NTNU
# NOTE: Changed by Johanne Glende to fit assignment.

# Table of Contents
# -----------------
# 1. Required Modules
# 2. Functions to print results

# 1. Required Modules
# -------------------
import sys
import math
import numpy
from sklearn import metrics

# 3. Functions to print results
# -----------------------------

def export_regression_results(actual_rewards, predicted_rewards, filename, algorithm_id, max_duration):
    output = open(filename, "a") # a (append) so that we get data from multiple algorithms in one file
    print_results(actual_rewards, predicted_rewards, output, algorithm_id, max_duration)
    output.close()
    
def print_results(actual_rewards, predicted_rewards, output, algorithm_id, max_duration):
    output.write(f"{algorithm_id.upper()}. Max duration: {max_duration}\n")   
    output.write("Actual duration\tPredicted duration\n")
    for i in range(0, len(actual_rewards)):
        output.write("\t\t{0:g}\t\t\t{1:g}\n".format(actual_rewards[i], round(predicted_rewards[i], 0)))
    output.write(f"\nData for {algorithm_id} (max duration: {max_duration}):\n")
    output.write("MAE\t{0:g}\n".format(round(metrics.mean_absolute_error(actual_rewards, predicted_rewards),3)))
    output.write("MSE\t{0:g}\n".format(round(math.sqrt(metrics.mean_squared_error(actual_rewards, predicted_rewards)),3)))
    output.write("R^2\t{0:g}\n".format(round(metrics.r2_score(actual_rewards, predicted_rewards),3)))
    output.write("\n------------------------------------------------------------\n")





