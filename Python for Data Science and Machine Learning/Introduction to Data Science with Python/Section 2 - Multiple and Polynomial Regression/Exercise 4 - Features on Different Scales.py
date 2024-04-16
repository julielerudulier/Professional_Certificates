import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Advertising.csv', index_col=0)
df.head()

X = df.drop('Sales', axis=1)
y = df.Sales.values

lm = LinearRegression().fit(X,y)

# you can learn more about Python format strings here:
# https://docs.python.org/3/tutorial/inputoutput.html
print(f'{"Model Coefficients":>9}')
for col, coef in zip(X.columns, lm.coef_):
    print(f'{col:>9}: {coef:>6.3f}')
print(f'\nR^2: {lm.score(X,y):.4}')

# From info on this kind of assignment statement see:
# https://python-reference.readthedocs.io/en/latest/docs/operators/multiplication_assignment.html
df *= 1000
df.head()

# refit a new regression model on the scaled data
X = df.drop('Sales', axis=1)
y = df.Sales.values
lm = LinearRegression().fit(X,y)

print(f'{"Model Coefficients":>9}')
for col, coef in zip(X.columns, lm.coef_):
    print(f'{col:>9}: {coef:>6.3f}')
print(f'\nR^2: {lm.score(X,y):.4}')

plt.figure(figsize=(8,3))
# column names to be displayed on the y-axis
cols = X.columns
# coeffient values from our fitted model (the intercept is not included)
coefs = lm.coef_
# create the horizontal barplot
plt.barh(cols, coefs)
# dotted, semi-transparent, black vertical line at zero
plt.axvline(0, c='k', ls='--', alpha=0.5)
# always label your axes
plt.ylabel('Predictor')
plt.xlabel('Coefficient Values')
# and create an informative title
plt.title('Coefficients of Linear Model Predicting Sales\n from Newspaper, '\
            'Radio, and TV Advertising Budgets (in Dollars)');


# Based on the plot above, advertising in which type of media has the largest effect on Sales?

A. Newspaper
B. Radio
C. TV

### edTest(test_Q1) ###
# your answer here
Q1_ANSWER = 'B' 


# If the newspaper advertising budget were higher, what difference might we expect to see in sales?

A. There would be no change
B. Sales would increase, but only slightly
C. Sales would decrease, but only slightly

### edTest(test_Q2) ###
# your answer here
Q2_ANSWER = 'C'


# create a new DataFrame to store the converted budgets
X2 = pd.DataFrame()
X2['TV (Rupee)'] = 200 * df['TV'] # convert to Sri Lankan Rupee
X2['Radio (Won)'] = 1175 * df['Radio'] # convert to South Korean Won
X2['Newspaper (Cedi)'] = 6 * df['Newspaper'] # Convert to Ghanaian Cedi

# we can use our original y as we have not converted the units for Sales
lm2 = LinearRegression().fit(X2,y)

print(f'{"Model Coefficients":>16}')
for col, coef in zip(X2.columns, lm2.coef_):
    print(f'{col:>16}: {coef:>8.5f}')
print(f'\nR^2: {lm2.score(X2,y):.4}')


# Assume that a $1 increase in the `Radio` budget is associated with an increase in `Sales` of $25. Then a 1 Won increase in the Radio budget would see Sales increase by ___ dollars.

Hint: 1,175 Won = $1

### edTest(test_Q3) ###
# your answer here
Q3_ANSWER = 0.0212


# How did your answer in Q3 compare to the original hypothetical increase of $25?

A. It was higher
B. It was lower
C. No change (scale invariant)

### edTest(test_Q4) ###
# your answer here
Q4_ANSWER = 'B'


plt.figure(figsize=(8,3))
plt.barh(X2.columns, lm2.coef_)
plt.axvline(0, c='k', ls='--', alpha=0.5)
plt.ylabel('Predictor')
plt.xlabel('Coefficient Values')
plt.title('Coefficients of Linear Model Predicting Sales\n from Newspaper, '\
            'Radio, and TV Advertising Budgets (Different Currencies)');


# Based on the plot above, which advertising in which type of media has the least effect on sales?

A. Newspaper
B. Radio
C. TV

### edTest(test_Q5) ###
# your answer here
Q5_ANSWER = 'B' 


# True or False: This is the same interpretation we had in our original model where all budgets were in dollars.

### edTest(test_Q6) ###
# Use the boolean values True or False
# your answer here
Q6_ANSWER = False


#  Imagine we have a 3rd regression models whose budgets have again been converted to 3 different currencies.
True or False: we can compare the 2nd and 3rd models' MSE losses to determine which model's coefficients provide a more accurate interpretation of what type of media advertising has the largest effect on Sales.

### edTest(test_Q7) ###
# Use the boolean values True or False
# your answer here
Q7_ANSWER = False


fig, axes = plt.subplots(2,1, figsize=(8,6), sharex=True)

axes[0].barh(X.columns, lm.coef_)
axes[0].set_title('Dollars');
axes[1].barh(X2.columns, lm2.coef_)
axes[1].set_title('Different Currencies')
for ax in axes:
    ax.axvline(0, c='k', ls='--', alpha=0.5)
axes[0].set_ylabel('Predictor')
axes[1].set_xlabel('Coefficient Values');


