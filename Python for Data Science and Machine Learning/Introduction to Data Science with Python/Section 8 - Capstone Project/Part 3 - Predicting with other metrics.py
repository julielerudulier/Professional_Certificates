# Import necessary libraries
import numpy as np 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
# Your code here

# Read the datafile "covid_train.csv"
df_train = pd.read_csv("covid_train.csv")

# Take a quick look at the dataframe
df_train.head(1)

# Read the datafile "covid_test.csv"
df_test = pd.read_csv("covid_test.csv")

# Take a quick look at the dataframe
df_test.head(1)

# Get the train predictors
x_train = df_train.drop(columns='Urgency')

# Get the train response variable
y_train = df_train['Urgency']

# Get the test predictors
x_test = df_test.drop(columns='Urgency')

# Get the test response variable
y_test = df_test['Urgency']

### edTest(test_model) ###
# Define a kNN classification model with k = 7
k_value = 7
knn_model = KNeighborsClassifier(n_neighbors = k_value)

# Fit the above model on the train data
knn_model.fit(x_train, y_train)

# Define a Logistic Regression model with max_iter as 10000 and C as 0.1 (leave all other parameters at default values)
log_model = LogisticRegression(max_iter = 10000, C=0.1)

# Fit the Logistic Regression model on the train data
log_model.fit(x_train, y_train)

y_log_pred = log_model.predict(x_test)
y_knn_pred = knn_model.predict(x_test)

log_cm = confusion_matrix(y_test, y_log_pred)
knn_cm = confusion_matrix(y_test, y_knn_pred)

#create the accuracy score
log_acc = accuracy_score(y_test, y_log_pred)
knn_acc = accuracy_score(y_test, y_knn_pred)

#create thge recall score
log_recall = recall_score(y_test, y_log_pred)
knn_recall = recall_score(y_test, y_knn_pred)

#specificity = TN / TN + FP
knn_spec = knn_cm[0][0] / (knn_cm[0][0] + knn_cm[0][1])
log_spec = log_cm[0][0] / (log_cm[0][0] + log_cm[0][1])

knn_prec = precision_score(y_test, y_knn_pred)
log_prec = precision_score(y_test, y_log_pred)

knn_f1 = f1_score(y_test, y_knn_pred)
log_f1 = f1_score(y_test, y_log_pred)

# Your code here
metric_scores = {
    'Accuracy' : [knn_acc, log_acc],
    'Recall' : [knn_recall, log_recall],
    'Specificity' : [knn_spec, log_spec],
    'Precision' : [knn_prec, log_prec],
    'F1-score' : [knn_f1, log_f1],
}

### edTest(test_metrics) ###
# Display your results
metric_scores
