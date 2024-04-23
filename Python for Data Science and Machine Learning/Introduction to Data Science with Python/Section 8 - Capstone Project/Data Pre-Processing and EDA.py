# Import necessary libraries

# Your code here
import numpy as np 
import pandas as pd
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Read the datafile "covid.csv"
df = pd.read_csv("covid.csv")

# Take a quick look at the dataframe
df.head()

# Check if there are any missing or Null values
df.isnull().sum()

### edTest(test_na) ###

# Find the number of rows with missing values
num_null = df.isnull().any(axis=1).sum()
print("Number of rows with null values:", num_null)

# kNN impute the missing data
# Use a k value of 5

# Your code here
# Create a list of all the column names
col_name = df.columns.unique().to_list()

# Mimic the df with a new variable impute df and make sure to add an index
x = df.drop(columns='Urgency')
y=df[['Urgency']]

x_new = x.copy()
y_new = y.copy()

x_new = pd.DataFrame(KNNImputer(n_neighbors = 5).fit_transform(x_new), columns=x_new.columns)

df_imputed = pd.concat([x_new, y], axis=1)
df_imputed.isnull().sum()

### edTest(test_impute) ###
# Replace the original dataframe with the imputed data, continue to use df for the dataframe

# Your code here
df = df_imputed

# Plot an appropriate graph to answer the following question
# Your code here
urgent_df = df[df['Urgency']==1]
bins = [20,30,40,50,60,70]

plt.hist(urgent_df, bins=bins, edgecolor='black')


### ⏸ Which age group has the most urgent need for a hospital bed?

#### A. 60 - 70 

#### B. 50 - 60 

#### C. 20 - 30

#### D. 40 - 50

### edTest(test_chow1) ###
# Submit an answer choice as a string below (eg. if you choose option A, put 'A')
answer1 = 'D'


# Plot an appropriate graph to answer the following question    
# Your code here
symp_df = urgent_df[['cough', 'fever', 'sore_throat', 'fatigue', 'Urgency']]
symp_counts = symp_df.drop(columns='Urgency').sum()

plt.bar(symp_counts.index, symp_counts.values, color='blue')

plt.xlabel('Symptoms')
plt.ylabel('Occurence')
plt.title('Frequency of Symptoms Leading to Urgency')


### ⏸ Among the following symptoms, which is the most common one for patients with urgent need of hospitalization?

#### A. Cough

#### B. Fever

#### C. Sore Throat

#### D. Fatigue

### edTest(test_chow2) ###
# Submit an answer choice as a string below (eg. if you choose option A, put 'A')
answer2 = 'B'


# Plot an appropriate graph to answer the following question    
# Your code here
new_df = df[df['Urgency']==0]
new_df = new_df.drop(columns='age')
cough_df = new_df.drop(columns='Urgency').sum()

plt.bar(cough_df.index, cough_df.values);


### ⏸ As compared to patients with urgent need of hospitalization, patients with no urgency have cough as a more common symptom?

#### A. True

#### B. False

#### C. It is the same

#### D. Cannot say

### edTest(test_chow3) ###
# Submit an answer choice as a string below (eg. if you choose option A, put 'A')
answer3 = 'A'


### edTest(test_split) ###
# Split the data into train and test sets with 70% for training
# Use random state of 60 and set of data as the train split

# Your code here
df_train, df_test = train_test_split(df, test_size=.3, random_state=60)

# Save the train data into a csv called "covid_train.csv"
# Remember to not include the default indices
df_train.to_csv('covid_train.csv', index=False)

# Save the test data into a csv called "covid_test.csv"
# Remember to not include the default indices
df_test.to_csv('covid_test.csv', index=False)
