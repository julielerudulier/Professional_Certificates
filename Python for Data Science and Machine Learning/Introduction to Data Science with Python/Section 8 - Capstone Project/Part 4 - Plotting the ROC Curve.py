# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
%matplotlib inline

# Read the datafile "covid_train.csv"
df_train = pd.read_csv('covid_train.csv')

# Take a quick look at the dataframe
df_train.head()

# Read the datafile "covid_test.csv"
df_test = pd.read_csv('covid_test.csv')

# Take a quick look at the dataframe
df_test.head()

### edTest(test_Xy) ###
# Get the train predictors
X_train = df_train.drop(columns='urgency')

# Get the train response variable
y_train = df_train['urgency']

# Get the test predictors
X_test = df_test.drop(columns='urgency')

# Get the test response variable
y_test = df_test['urgency']

### edTest(test_kNN) ###
# Define a kNN classification model with k = 7
knn = KNeighborsClassifier(n_neighbors = 7)

# Fit the above model on the train data
knn.fit(X_train, y_train)

# Predict probabilities for the positive class on the test data using the kNN model
y_pred_knn = knn.predict_proba(X_test)[:,1]

### edTest(test_logreg) ###
# Define a Logistic Regression model with max_iter as 10000, C as 0.1, and a random_state of 42
logreg = LogisticRegression(max_iter=10000, C=0.1, random_state=42)

# Fit the Logistic Regression model on the train data
logreg.fit(X_train, y_train)

# Predict probabilities for the positive class on the test data using the logistic regression model
y_pred_logreg = logreg.predict_proba(X_test)[:,1]

def get_thresholds(y_pred_proba):
    # We only need to consider unique predicted probabilities
    unique_probas = np.unique(y_pred_proba)
  
    # Sort unique probabilities in descending order
    unique_probas_sorted = sorted(unique_probas, reverse=True)
   
    # We'll also add some additional thresholds to our set
    # This ensures our ROC curves reach the corners of the plot, (0,0) and (1,1)
    
    # Insert 1.1 at the beginning of the threshold array
    # 1.1 may seem like an odd threshold, but a value greater than 1
    # is required if we want the ROC curve to reach the lower left corner
    # (0 fpr, 0 tpr) considering one of our models produces probability predictions of 1
    thresholds = np.insert(unique_probas_sorted, 0, 1.1)
  
    # Append 0 to the end of the thresholds
    thresholds = np.append(thresholds, 0)
    return thresholds

### edTest(test_thresholds) ###
knn_thresholds = get_thresholds(y_pred_knn)

logreg_thresholds = get_thresholds(y_pred_logreg)

### edTest(test_fpr) ###
def get_fpr(y_true, y_pred_proba, threshold):
    # your code here
    fpr_list = []
    y_pred = []
  
    for prob in y_pred_proba:
            if prob >= threshold:
                y_pred.append(1)
            else:
                y_pred.append(0)
              
    cm = confusion_matrix(y_true, y_pred)
    fpr = cm[0][1] / (cm[0][1]+cm[0][0])
    fpr_list.append(fpr)
  
    return fpr

### edTest(test_tpr) ###
def get_tpr(y_true, y_pred_proba, threshold):
    # your code here
    y_pred = []
        
    for prob in y_pred_proba:
        if prob >= threshold:
            y_pred.append(1)
        else:
            y_pred.append(0)
          
    cm = confusion_matrix(y_true, y_pred)
    tpr = cm[1][1] / (cm[1][1]+cm[1][0])
  
    return tpr

### edTest(test_fpr_tpr) ###
# FPR for the kNN at each of its thresholds
knn_fpr = []
for threshold in knn_thresholds:
    knn_fpr.append(get_fpr(y_test, y_pred_knn, threshold))

# TPR for the kNN at each of its thresholds
knn_tpr = []
for threshold in knn_thresholds:
    knn_tpr.append(get_tpr(y_test, y_pred_knn, threshold))

# TPR for the logistic model at each of its thresholds
logreg_tpr = []
for threshold in logreg_thresholds:
    logreg_tpr.append(get_tpr(y_test, y_pred_logreg, threshold))

# FPR for the logistic model at each of its thresholds
logreg_fpr = []
for threshold in logreg_thresholds:
    logreg_fpr.append(get_fpr(y_test, y_pred_logreg, threshold))

### edTest(test_auc) ###
# Compute the ROC AUC score of the Logistic model
knn_auc = roc_auc_score(y_test, y_pred_knn)

# Compute the ROC AUC score of the kNN model
logreg_auc = roc_auc_score(y_test, y_pred_logreg)

### edTest(test_plot) ###
# Area under curve - Logistic Regression & kNN
fig, ax = plt.subplots(figsize = (14,8))

# Plot KNN Regression ROC Curve
ax.plot(knn_fpr,
        knn_tpr,
        label=f'KNN (area = {knn_auc:.2f})',
        color='g',
        lw=3)

# Plot Logistic Regression ROC Curve
ax.plot(logreg_fpr,
        logreg_tpr,
        label=f'Logistic Regression (area = {logreg_auc:.2f})',
        color = 'purple',
        lw=3)

# Threshold annotations
label_kwargs = {}
label_kwargs['bbox'] = dict(
    boxstyle='round, pad=0.3', color='lightgray', alpha=0.6
)
eps = 0.02 # offset
for i in range(0, len(logreg_fpr),15):
    threshold = str(np.round(logreg_thresholds[i], 2))
    ax.annotate(threshold, (logreg_fpr[i], logreg_tpr[i]-eps), fontsize=12, color='purple', **label_kwargs)

for i in range(0, len(knn_fpr)-1):
    threshold = str(np.round(knn_thresholds[i], 2))
    ax.annotate(threshold, (knn_fpr[i], knn_tpr[i]+eps), fontsize=12, color='green', **label_kwargs)

# Plot diagonal line representing a random classifier
ax.plot([0, 1], [0, 1], 'k--', label='Random Classifier')

# Scenario 1 - Brazil
ax.fill_between([0,0.5],[0.5,0], color = 'red', alpha = 0.4, label='Scenario 1 - Brazil');

# Scenario 2 - Germany
ax.axhspan(0.8, 0.9, facecolor='y', alpha=0.4, label = 'Scenario 2 - Germany');

# Scenario 3 - India
ax.fill_between([0,1],[1,0],[0.5,-0.5], alpha = 0.4, color = 'blue', label = 'Scenario 3 - India');

ax.set_xlim([0.0, 1.0]);
ax.set_ylim([0.0, 1.05]);
ax.set_xlabel('False Positive Rate', fontsize=20)
ax.set_ylabel('True Positive Rate', fontsize=20)
ax.set_title('Receiver Operating Characteristic', fontsize=20)
ax.legend(loc="lower right", fontsize=15)
plt.show()
