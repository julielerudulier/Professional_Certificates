# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# "Advertising.csv" containts the data set used in this exercise
data_filename = 'Advertising.csv'

# Read the file "Advertising.csv" file using the pandas library
df = pd.read_csv(data_filename)

# Get a quick look of the data
df.head()

### edTest(test_pandas) ###
# Create a new dataframe by selecting the first 7 rows of
# the current dataframe
df_new = df.iloc[:7]

# Print your new dataframe to see if you have selected 7 rows correctly
print(df_new)

# Use a scatter plot for plotting a graph of TV vs Sales
plt.scatter(df_new['Sales'], df_new['TV'])

# Add axis labels for clarity (x : TV budget, y : Sales)
plt.xlabel("TV budget")
plt.ylabel("Sales")

# Add plot title 
plt.title("TV Ads vs Sales")
