# import libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

# colour palette
BLUEBIRD_AZURE = "#007FFF"
BLUEBIRD_LIGHT = "#4DA3FF"
BLUEBIRD_DARK = "#005FCC"
BLUEBIRD_PALETTE = [
    BLUEBIRD_AZURE,
    BLUEBIRD_LIGHT,
    BLUEBIRD_DARK
]

# load the dataset
combined_data_scaled = pd.read_csv('combined_data_scaled.csv')

#convert date column to datetime
combined_data_scaled['Date'] = pd.to_datetime(combined_data_scaled['Date'])

# define the 37 month dataset
combined_36_scaled = combined_data_scaled.loc[(combined_data_scaled['Date'] >= '2020-08-01') & (combined_data_scaled['Date'] < '2023-09-01')]

# everything combined
plt.figure(figsize = (12,10))
plt.plot(combined_36_scaled['Date'], combined_36_scaled['avg_luxury'], color = BLUEBIRD_LIGHT, label = 'Average luxury prices', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.plot(combined_36_scaled['Date'], combined_36_scaled['UK'], color = BLUEBIRD_DARK, label = 'Average house price', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.plot(combined_36_scaled['Date'], combined_36_scaled['Price'], color = 'black', label = 'FTSE 350', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Value', fontsize = 20)
plt.xticks(fontsize = 20, rotation = 45)
plt.yticks(fontsize = 20)
plt.title('Prices each month', fontsize = 20)
plt.axvline(pd.to_datetime('2022-02-01'), color = 'red', linewidth = 15)

# FTSE 350 vs Luxury
plt.figure(figsize = (12,10))
plt.plot(combined_36_scaled['Date'], combined_36_scaled['avg_luxury'], color = BLUEBIRD_LIGHT, label = 'Luxury value', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.plot(combined_36_scaled['Date'], combined_36_scaled['Price'], color = 'black', label = 'FTSE 350', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Value', fontsize = 20)
plt.xticks(fontsize = 20, rotation = 45)
plt.yticks(fontsize = 20)
plt.title('Prices each month', fontsize = 20)
plt.axvline(pd.to_datetime('2022-02-01'), color = 'red', linewidth = 15)
plt.legend(fontsize = 20, loc = 'upper right', bbox_to_anchor = (1.03, 0.6))

# FTSE 350 vs General
plt.figure(figsize = (12,10))
plt.plot(combined_36_scaled['Date'], combined_36_scaled['UK'], color = BLUEBIRD_DARK, label = 'Average house price', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.plot(combined_36_scaled['Date'], combined_36_scaled['Price'], color = 'black', label = 'FTSE 350', linewidth = 2, linestyle = '-', marker = 'o', markersize = 15)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Value', fontsize = 20)
plt.xticks(fontsize = 20, rotation = 45)
plt.yticks(fontsize = 20)
plt.title('Prices each month', fontsize = 20)
plt.axvline(pd.to_datetime('2022-02-01'), color = 'red', linewidth = 15)
plt.legend(fontsize = 20)