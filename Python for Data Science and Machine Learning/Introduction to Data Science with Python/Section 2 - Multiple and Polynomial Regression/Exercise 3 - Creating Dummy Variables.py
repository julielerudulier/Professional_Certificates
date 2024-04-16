import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the credit data.
df = pd.read_csv('credit.csv')
df.head()

# The response variable will be 'Balance.'
x = df.drop('Balance', axis=1)
y = df['Balance']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Trying to fit on all features in their current representation throws an error.
try:
    test_model = LinearRegression().fit(x_train, y_train)
except Exception as e:
    print('Error!:', e)


# Given this error and what you've seen of the data so far, what do you think the problem is?

A. We are trying to fit on too many features/columns
B. Some columns are strings
C. The column names contain capital letters
D. The features are on different scales

### edTest(test_chow1) ###
# Submit an answer choice as a string below.
answer1 = 'B'


# Inspect the data types of the DataFrame's columns.
df.dtypes

### edTest(test_model1) ###
# Fit a linear model using only the numeric features in the dataframe.
numeric_features = ['Income','Limit','Rating','Cards','Age','Education']
model1 = LinearRegression().fit(x_train[numeric_features], y_train)

# Report train and test R2 scores.
train_score = model1.score(x_train[numeric_features], y_train)
test_score = model1.score(x_test[numeric_features], y_test)
print('Train R2:', train_score)
print('Test R2:', test_score)

# Look at unique values of Ethnicity feature.
print('In the train data, Ethnicity takes on the values:', list(x_train['Ethnicity'].unique()))


# From the output above, how many binary variables will be required to encode the Ethnicity feature?

A. 1
B. 2
C. 3
D. 4

### edTest(test_chow2) ###
# Submit an answer choice as a string below.
answer2 = 'B'


### edTest(test_design) ###
# Create x train and test design matrices creating dummy variables for the categorical.
# hint: use pd.get_dummies() with the drop_first hyperparameter for this
x_train_design = pd.get_dummies(x_train, drop_first=True)
x_test_design = pd.get_dummies(x_test, drop_first=True)
x_train_design.head()

# Confirm that all data types are now numeric.
x_train_design.dtypes

### edTest(test_model2) ###
# Fit model2 on design matrix
model2 = LinearRegression().fit(x_train_design, y_train)

# Report train and test R2 scores
train_score = model2.score(x_train_design, y_train)
test_score = model2.score(x_test_design, y_test)
print('Train R2:', train_score)
print('Test R2:', test_score)


# How do the R2 scores of the two models compare?

A. numeric only model performs better on both train and test.
B. numeric only model performs better on train but worse on test.
C. full model performs better on both train and test.
D. full model performs better on train but worse on test.

### edTest(test_chow3) ###
# Submit an answer choice as a string below.
answer3 = 'C'


# Note that the intercept is not a part of .coef_ but is instead stored in .intercept_.
coefs = pd.DataFrame(model2.coef_, index=x_train_design.columns, columns=['beta_value'])
coefs

# Visualize crude measure of feature importance.
sns.barplot(data=coefs.T, orient='h').set(title='Model Coefficients');


# Base, on the plot above, which categorical feature has the strongest relationship with Balance?

A. Cards
B. Gender_Female
C. Student_Yes
D. Ethnicity_Caucasian

### edTest(test_chow4) ###
# Submit an answer choice as a string below.
answer4 = 'C'


### edTest(test_model3) ###
# Specify best categorical feature
best_cat_feature = 'Student_Yes'

# Define the model.
features = ['Income', best_cat_feature]
model3 = LinearRegression()
model3.fit(x_train_design[features], y_train)

# Collect betas from fitted model.
beta0 = model3.intercept_
beta1 = model3.coef_[features.index('Income')]
beta2 = model3.coef_[features.index(best_cat_feature)]

# Display betas in a DataFrame.
coefs = pd.DataFrame([beta0, beta1, beta2], index=['Intercept']+features, columns=['beta_value'])
coefs

# Visualize crude measure of feature importance.
sns.barplot(data=coefs.T, orient='h').set(title='Model Coefficients');

### edTest(test_prediction_lines) ###
# Create space of x values to predict on.
x_space = np.linspace(x['Income'].min(), x['Income'].max(), 1000)

# Generate 2 sets of predictions based on best categorical feature value.
# When categorical feature is true/present (1)
y_hat_yes = 177.658909 + 6.773090 * x_space + 1 * 371.895694
# When categorical feature is false/absent (0)
y_hat_no = 177.658909 + 6.773090 * x_space + 0 * 371.895694

# Plot the 2 prediction lines for students and non-students.
ax = sns.scatterplot(data=pd.concat([x_train_design, y_train], axis=1), x='Income', y='Balance', hue=best_cat_feature, alpha=0.8)
ax.plot(x_space, y_hat_no)
ax.plot(x_space, y_hat_yes);


# What is the effect of student status on the regression line?

A. Non-students' balances increase faster with raising income (i.e., steeper slope)
B. Students' balances increase faster with raising income (i.e., steeper slope)
C. Non-students' higher balances on average (i.e., higher intercept)
D. students' higher balances on average (i.e., higher intercept)

### edTest(test_chow5) ###
# Submit an answer choice as a string below.
answer5 = 'D'

