# import important libraries
%matplotlib inline
import sys
import numpy as np
import pandas as pd
from math import exp
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score

# Make a dataframe of the file "insurance_claim.csv"
data_filename = 'insurance_claim.csv'
df = pd.read_csv(data_filename)

# Take a quick look of the data, notice that the response variable is binary
df.head()

# Assign age as the predictor variable 
x = df["age"].values

# Assign insuranceclaim as the response variable
y = df["insuranceclaim"].values

# Make a plot of the response (insuranceclaim) vs the predictor (age)
plt.plot(x,y,'o', markersize=7,color="#011DAD",label="Data")

# Add the labels for the axes
plt.xlabel("Age")
plt.ylabel("Insurance claim")

plt.xticks(np.arange(18, 80, 4.0))

# Label the value 1 as 'Yes' & 0 as 'No'
plt.yticks((0,1), labels=('No', 'Yes'))
plt.legend(loc='best')
plt.show()

### edTest(test_beta_guesstimate) ###
# Guesstimate the values of 𝛽0 & 𝛽1

beta0 = -1
beta1 = 0.026

### edTest(test_beta_computation) ###
def logistic(x):
    z = beta0 + (beta1 * x)
    return 1 / (1 + np.exp(-z))
    
# P(y=1|x_i) for each x_i in x
probas = [logistic(item) for item in x]

# Get classification predictions
y_pred = []
for item in probas:
    if item > 0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)

### edTest(test_acc) ###
# Use accuracy_score function to find the accuracy 
accuracy = accuracy_score(y_pred, y)

# Print the accuracy
print(accuracy)

# Make a plot similar to the one above along with the fit curve
plt.plot(x, y,'o', markersize=7, color="#011DAD", label="Data")

plt.plot(x, y_pred,linewidth=2, color='black', label="Classifications")
plt.plot(x, probas,linewidth=2, color='red', label="Probabilities")

plt.xticks(np.arange(18, 80, 4.0))
plt.xlabel("Age")
plt.ylabel("Insurance claim")
plt.yticks((0, 1), labels=('No', 'Yes'))
plt.legend()
plt.show()
