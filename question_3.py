# import libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
import numpy as np

# load the dataset
combined_data = pd.read_csv('combined_data.csv')

#convert date column to datetime
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# define prewar and postwar datasets
pre_war = combined_data.loc[(combined_data['Date'] >= '2020-08-01') & (combined_data['Date'] < '2022-02-01')]
post_war = combined_data.loc[(combined_data['Date'] >= '2022-03-01') & (combined_data['Date'] < '2023-09-01')]

# calculate the correlations for the general housing market
pre_war_general = pre_war['Price'].corr(pre_war['UK'])
post_war_general = post_war['Price'].corr(post_war['UK'])

# calculate the correlations for the luxury market
pre_war_luxury = pre_war['Price'].corr(pre_war['avg_luxury'])
post_war_luxury = post_war['Price'].corr(post_war['avg_luxury'])

# define the function
def fisher_test(r1, r2, n1 = 18, n2 = 18):
    # Step 1: Transform r to z
    z1, z2 = np.arctanh(r1), np.arctanh(r2)
    # Step 2: Standard Error
    se = np.sqrt(1/(n1-3) + 1/(n2-3))
    # Step 3: Z-statistic
    z_stat = (z1 - z2) / se
    # Step 4: P-value
    p_val = 2 * (1 - norm.cdf(abs(z_stat)))
    return z_stat, p_val

# calculate Fisher test for general housing prices
z, p = fisher_test(pre_war_general, post_war_general)
print(f"FTSE vs General: Z={z:.2f}, p-value={p:.4f}")

# calculate Fisher test for luxury prices
z, p = fisher_test(pre_war_luxury, post_war_luxury)
print(f"FTSE vs Luxury: Z={z:.2f}, p-value={p:.4f}")