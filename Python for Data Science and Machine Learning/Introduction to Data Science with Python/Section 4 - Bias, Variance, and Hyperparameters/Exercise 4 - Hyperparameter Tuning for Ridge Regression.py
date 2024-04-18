# Import required libraries
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# These are custom functions made to help you visualise your results
from helper import plot_functions
from helper import plot_coefficients

# Open the file 'polynomial50.csv' as a dataframe
df = pd.read_csv('polynomial50.csv')

# Take a quick look at the data
df.head()

# Assign the values of the 'x' column as the predictor
x = df[['x']].values

# Assign the values of the 'y' column as the response
y = df['y'].values

# Also assign the true value of the function (column 'f') to the variable f 
f = df['f'].values

# Visualise the distribution of the x, y values & also the value of the true function f
fig, ax = plt.subplots()

# Plot x vs y values
ax.plot(x, y, '.', label = 'Observed values',markersize=10)

# Plot x vs true function value
ax.plot(x, f, 'k-', label = 'Function description')

# The code below is to annotate your plot
ax.legend(loc = 'best');
ax.set_xlabel('Predictor - $X$',fontsize=16)
ax.set_ylabel('Response - $Y$',fontsize=16)
ax.set_title('Predictor vs Response plot',fontsize=16);

# Split the data into train and validation sets with training size 80% and random_state = 109
x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.8, random_state=109)

### edTest(test_mse) ### 
fig, rows = plt.subplots(6, 2, figsize=(16, 24))

# Select the degree for polynomial features
degree = 2

# List of hyper-parameter values 
alphas = [0.0, 1e-7, 1e-5, 1e-3, 0.1, 1]

# Create two lists for training and validation error
training_error, validation_error = [],[]

# Compute the polynomial features train and validation sets
x_poly_train = PolynomialFeatures(degree).fit_transform(x_train)
x_poly_val= PolynomialFeatures(degree).fit_transform(x_val)

for i, alpha in enumerate(alphas):
    l,r = rows[i]
    
    # For each i, fit a ridge regression on training set
    ridge_reg = Ridge(fit_intercept=False, alpha=alpha)
    ridge_reg.fit(x_poly_train, y_train)
    
    # Predict on the validation set 
    y_train_pred = ridge_reg.predict(x_poly_train)
    y_val_pred = ridge_reg.predict(x_poly_val)
    
    # Compute the training and validation errors
    mse_train = mean_squared_error(y_train_pred, y_train) 
    mse_val = mean_squared_error(y_val_pred, y_val)
    
    # Add that value to the list 
    training_error.append(mse_train)
    validation_error.append(mse_val)
    
    # Use helper functions plot_functions & plot_coefficients to visualise the plots
    plot_functions(degree, ridge_reg, l, df, alpha, x_val, y_val, x_train, y_train)
    plot_coefficients(ridge_reg, r, alpha)

sns.despine()

### edTest(test_hyper) ###
# Find the best value of hyper parameter, which gives the least error on the validdata
best_parameter = 1
print(f'The best hyper parameter value, alpha = {best_parameter}')
