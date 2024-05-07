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

def export_results(actual_rewards, predicted_rewards, filename):
    output = open(filename, "a") # a (append) so that we get data from multiple algorithms in one file
    print_results(actual_rewards, predicted_rewards, output)
    output.close()
    
def print_results(actual_rewards, predicted_rewards, output):
    output.write("Actual duration\tPredicted duration\n")
    for i in range(0, len(actual_rewards)):
        output.write("{0:g}\t{1:g}\n".format(actual_rewards[i], round(predicted_rewards[i], 0)))
    output.write("\n")
    output.write("MAE\t{0:g}\n".format(metrics.mean_absolute_error(actual_rewards, predicted_rewards)))
    output.write("RMSE\t{0:g}\n".format(math.sqrt(metrics.mean_squared_error(actual_rewards, predicted_rewards))))
    output.write("R^2\t{0:g}\n".format(metrics.r2_score(actual_rewards, predicted_rewards)))





