# Import necessary libraries
# Your code here
import numpy as np 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score

# Read the datafile "covid_train.csv"
df_train = pd.read_csv('covid_train.csv')

# Take a quick look at the dataframe
df_train.head()

# Read the datafile "covid_test.csv"
df_test = pd.read_csv('covid_test.csv')

# Take a quick look at the dataframe
df_test.head()

# Get the train predictors
X_train = df_train.drop(columns='Urgency')

# Get the train response variable
y_train = df_train[['Urgency']]

# Get the test predictors
X_test = df_test.drop(columns='Urgency')

# Get the test response variable
y_test = df_test[['Urgency']]

### edTest(test_model) ###

# Define your classification model
k_value = 5
model = KNeighborsClassifier(n_neighbors=k_value)

# Fit the model on the train data
model.fit(X_train, y_train)

### edTest(test_accuracy) ###

# Predict and compute the accuracy on the test data
y_pred = model.predict(X_test)

model_accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy is {model_accuracy}")
