# Import libraries
import pandas as pd
import numpy as np

# Datasets
ftse_350 = pd.read_csv('ftse_350_monthly.csv')
price_paid = pd.read_csv('price_paid_monthly.csv')
uk_stability = pd.read_csv('uk_stability_M.csv')
sanctioned = pd.read_csv('sanctioned_monthly.csv')
house_price_index = pd.read_csv('cleaned_uk_houseprice_index.csv')
house_price = pd.read_csv('cleaned_uk_houseprice_sheet2.csv')

# Stock market
closing_price = pd.DataFrame()
closing_price['Date'] = ftse_350['Date']
closing_price['Price'] = ftse_350['Price']
closing_price['Date'] = pd.to_datetime(closing_price['Date'])

# Luxury market
price_paid['Date'] = pd.to_datetime(price_paid['month'])
price_paid = price_paid.drop('month', axis = 1)
# create a new metric for luxury market
price_paid['avg_luxury'] = price_paid['total_value']/price_paid['property_count']

# combining stock and luxury market
combined_data = closing_price.merge(price_paid, how = 'left', on = 'Date' )

# Sanctions
sanctioned['Date'] = pd.to_datetime(sanctioned['month'])
sanctioned = sanctioned.drop('month', axis = 1)

# add sanctions data to combined dataset
combined_data = combined_data.merge(sanctioned, how = 'left', on = 'Date')

# filling the missing values in the sanctions dataset
combined_data = combined_data.fillna(0)

# General House Price
house_price['Date'] = pd.to_datetime(house_price['Date'])
house_price_means = pd.DataFrame()
house_price_means['Date'] = house_price['Date']
house_price_means['UK'] = house_price['United Kingdom']
house_price_means['London'] = house_price['London']

# add general house price data to combined dataset
combined_data = combined_data.merge(house_price_means, how = 'left', on = 'Date')

# convert to csv file
combined_data.to_csv('combined_data.csv' index = False)
