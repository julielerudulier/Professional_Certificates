# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper import fit_and_plot_linear, fit_and_plot_multi
%matplotlib inline

# Read the file "Advertising.csv"
df = pd.read_csv('Advertising.csv')

# Take a quick look at the dataframe
df.head()

# Define an empty Pandas dataframe to store the R-squared value associated with each 
# predictor for both the train and test split
df_results = pd.DataFrame(columns=['Predictor', 'R2 Train', 'R2 Test'])
df_results

# For each predictor in the dataframe, call the function "fit_and_plot_linear()"
# from the helper file with the predictor as a parameter to the function

# This function will split the data into train and test split, fit a linear model
# on the train data and compute the R-squared value on both the train and test data

# **Your code here**
r2_train_TV, r2_test_TV = fit_and_plot_linear(df[['TV']])
r2_train_Radio, r2_test_Radio = fit_and_plot_linear(df[['Radio']])
r2_train_Newspaper, r2_test_Newspaper = fit_and_plot_linear(df[['Newspaper']])


# Based on the plot and results, which model do you think is the best for prediction?

A. TV
B. Radio
C. Newspaper
D. Sales

### edTest(test_chow1) ###
# Submit an answer choice as a string below 
# (Eg. if you choose option C, put 'C')
answer1 = 'A'

# Call the function "fit_and_plot_multi()" from the helper to fit a multilinear model
# on the train data and compute the R-squared value on both the train and test data

# **Your code here**
r2_train_Multi, r2_test_Multi = fit_and_plot_multi()

### edTest(test_dataframe) ###

# Store the R-squared values for all models
# in the dataframe intialized above
# **Your code here**
df_results.loc[0] = ['TV', r2_train_TV, r2_test_TV]
df_results.loc[1] = ['Radio', r2_train_Radio, r2_test_Radio]
df_results.loc[2] = ['Newspaper', r2_train_Newspaper, r2_test_Newspaper]
df_results.loc[3] = ['Multilinear', r2_train_Multi, r2_test_Multi]

# Take a quick look at the dataframe
df_results.head()


# Why do you think the mutilinear regression model is better?

A. The model goes to the gym thrice as more when compare to the linear model.
B. The model has more information from various predictors/features.
C. The model is not linear, hence fits the complex data.
D. The model is not better than the simple linear regression.

### edTest(test_chow2) ###
# Submit an answer choice as a string below 
# (Eg. if you choose option C, put 'C')
answer2 = 'B'
