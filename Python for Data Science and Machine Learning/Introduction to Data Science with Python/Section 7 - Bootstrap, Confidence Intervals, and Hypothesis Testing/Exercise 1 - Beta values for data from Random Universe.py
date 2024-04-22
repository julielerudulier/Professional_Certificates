# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from randomuniverse import RandomUniverse
%matplotlib inline

# Read the advertising dataset as a pandas dataframe
df = pd.read_csv('Advertising_adj.csv')

# Take a quick look at the dataframe
df.head()

# Create two empty lists that will store the beta values
beta0_list, beta1_list = [],[]

# Choose the number of "parallel" Universes to generate 
# that many new versions of the dataset
parallelUniverses = 500

# Loop over the maximum number of parallel Universes
for i in range(parallelUniverses):

    # Call the RandomUniverse helper function with the dataframe
    # read from the data file
    df_new = RandomUniverse(df)

    # Find the mean of the predictor values i.e. tv
    xmean = df_new.tv.mean()

    # Find the mean of the response values i.e. sales
    ymean = df_new.sales.mean()

    # Compute the analytical values of beta0 and beta1 using the 
    # equation given in the hints
    beta1 = np.sum((df_new.tv-xmean)*(df_new.sales-ymean))/np.sum((df_new.tv - xmean)**2)
    beta0 = ymean-(beta1*xmean)

    # Append the calculated values of beta1 and beta0 to the appropriate lists
    beta0_list.append(beta0)
    beta1_list.append(beta1)

### edTest(test_beta) ###
# Compute the mean of the beta values
beta0_mean = np.mean(beta0_list)
beta1_mean = np.mean(beta1_list)

# Plot histograms of beta_0 and beta_1 using lists created above 
fig, ax = plt.subplots(1,2, figsize=(18,8))
ax[0].hist(beta0_list)
ax[1].hist(beta1_list)
ax[0].set_xlabel('Beta 0')
ax[1].set_xlabel('Beta 1')
ax[0].set_ylabel('Frequency');

### edTest(test_chow1) ###
# Submit an answer choice as a string below 
# (Eg. if you choose option C, put 'C')
answer1 = 'D'
