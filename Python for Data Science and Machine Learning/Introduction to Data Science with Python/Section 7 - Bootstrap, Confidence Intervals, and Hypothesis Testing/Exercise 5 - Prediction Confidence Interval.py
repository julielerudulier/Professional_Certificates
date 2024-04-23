# Import libraries
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy import stats

# Read the `Advertising.csv` dataframe
df = pd.read_csv('Advertising.csv')
df.head()

# This helper function computes the variance of the error term 
def error_func(y,y_p):
    n = len(y)
    return np.sqrt(np.sum((y-y_p)**2/(n-2)))

# select the number of bootstraps 
numboot = 1000

# Set the budget amount of $1000. We have used a 2d list to facilitate model prediction (sklearn.LinearRegression requires input as a 2d array)
budget = [[1000]]

# Define an empty list that will store sales predictions for each bootstrap
sales_dist = []

# Running through each bootstrap, we fit a model, make predictions and compute 
#sales which is appended to the list defined above

for i in range(numboot):
    # Bootstrap using df.sample method.
    df_new = df.sample(frac=1, replace=True)
    x = df_new[['TV']].values
    y = df_new['Sales'].values
    linreg = LinearRegression()
    linreg.fit(x,y)
    prediction = linreg.predict(budget)
    y_pred = linreg.predict(x) 
    error = np.random.normal(0,error_func(y, y_pred))
  
    # The final sales prediction is the sum of the model prediction and the error term
    sales = prediction + error
    sales_dist.append(np.float64(sales))

### edTest(test_sales) ###
# We sort the list containing sales predictions in ascending values 
sales_dist.sort()

# find the 95% confidence interval using np.percentile function at 2.5% and 97.5%
sales_CI = (np.percentile(sales_dist, 2.5), np.percentile(sales_dist, 97.5))

# Use this helper function to plot the histogram of beta values along with the 95% confidence interval
def plot_simulation(simulation,confidence):
    plt.hist(simulation, bins = 30, label = 'beta distribution', align = 'left', density = True, edgecolor='k')
    plt.axvline(confidence[1], 0, 1, color = 'r', label = 'Right Interval')
    plt.axvline(confidence[0], 0, 1, color = 'red', label = 'Left Interval')
    plt.xlabel('Beta value')
    plt.ylabel('Frequency')
    plt.legend(frameon = False, loc = 'upper right')

# call the function above with the computed sales distribution and the confidence intervals from earlier
plot_simulation(sales_dist, sales_CI)

# Print the computed values
print(f"With a TV advertising budget of ${budget[0][0]},")
print(f"we can expect an increase of sales anywhere between {sales_CI[0]:0.2f} to {sales_CI[1]:.2f}\
 with a 95% confidence interval")
