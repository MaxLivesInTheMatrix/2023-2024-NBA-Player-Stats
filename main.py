import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Start with the path to the stats files
stats = '/Users/max/gitRepositories/2023-2024-NBA-Player-Stats/nba-player-data.csv'

dataFrame = pd.read_csv(stats)
dataFrame['MP'] = pd.to_numeric(dataFrame['MP'], errors='coerce')

# Drop rows where the first column is the header again
dataFrame = dataFrame[dataFrame['Rk'] != 'Rk']

# Convert numeric columns to proper data types
df = dataFrame.apply(pd.to_numeric, errors='ignore')

print(dataFrame.head())
print()
print(dataFrame.info())
print()
print(dataFrame.describe())

# First lets try something simple, like a histogram of ages

customBins = []              # Bins for ages from 18 to 40
for age in range(18, 41, 2):
    customBins.append(age)
    
bin_labels = [f'{customBins[i]}-{customBins[i+1]}' for i in range(len(customBins)-1)] # Create an array of strings with ages as buckets. Literally: ["18-20", "20-22", etc]

plt.figure(figsize=(12, 6))  # Plot dimensions

tmp = df['Age'].plot.hist(bins=customBins, density=False, color='red', edgecolor='black') # Creating the plot before showing it

# Add bin labels
for i in range(len(bin_labels)):
    plt.text((customBins[i] + customBins[i + 1]) / 2, tmp.patches[i].get_height(), # The first part of the expression gets the middle of the bin,
                                                                                   # the patches attribute contains the bars of the histrogram
                                                                                   # get_height is a built in matplotlib method
                                                                                   # ha is horizontal alignment and va is vertical alignment
             int(tmp.patches[i].get_height()), ha='center', va='bottom')
    
plt.style.use('ggplot') # makes plot looks much nicer
plt.xlabel('Age')
plt.ylabel('Number of Players')
plt.title('Distribution of Player Ages in the NBA')
plt.xticks([customBins[i] + (customBins[i + 1] - customBins[i]) / 2 for i in range(len(customBins) - 1)], bin_labels)
plt.show()