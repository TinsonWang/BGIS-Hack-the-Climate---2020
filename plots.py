import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dataset = dataset.loc[ (dataset['State'] == 'CA') |
#                        (dataset['State'] == 'OR') |
#                        (dataset['State'] == 'NV') |
#                        (dataset['State'] == 'AZ') ]

# plt.xlabel("Year")
# plt.ylabel("Natural Gas Consumption (Billion BTU)")
# plt.title("Natural Gas Consumption in the state of California and its neighbouring states from 1960-2017")
#
# labels = [ 'California', 'Orgeon', 'Nevada', 'Arizona' ]
#
# dataset_CA = dataset.loc[ (dataset['State'] == 'CA' ) ]
# x = dataset_CA[['X', 'Y', 'Year']].values.reshape(-1, 3)
# y = dataset_CA['NatGasC'].str.replace(",", "").astype(int).values.reshape(-1, 1)
# plt.scatter( x[:, 2], y, c='b', label='California')
#
# dataset_OR = dataset.loc[ (dataset['State'] == 'OR') ]
# x = dataset_OR[['X', 'Y', 'Year']].values.reshape(-1, 3)
# y = dataset_OR['NatGasC'].str.replace(",", "").astype(int).values.reshape(-1, 1)
# plt.scatter( x[:, 2], y, c='r', label='Oregon')
#
# dataset_NV = dataset.loc[ (dataset['State'] == 'NV') ]
# x = dataset_NV[['X', 'Y', 'Year']].values.reshape(-1, 3)
# y = dataset_NV['NatGasC'].str.replace(",", "").astype(int).values.reshape(-1, 1)
# plt.scatter( x[:, 2], y, c='g', label='Nevada')
#
# dataset_AZ = dataset.loc[ (dataset['State'] == 'AZ') ]
# x = dataset_AZ[['X', 'Y', 'Year']].values.reshape(-1, 3)
# y = dataset_AZ['NatGasC'].str.replace(",", "").astype(int).values.reshape(-1, 1)
# plt.scatter( x[:, 2], y, c='m', label='Arizona')
#
# plt.legend()
# plt.show()

# dataset_US = pd.read_csv("usa_natgas_prices.csv")
# x = dataset_US['Year'].values.reshape(-1, 1)
# y = dataset_US['Prices'].values.reshape(-1, 1)
# plt.title("Natural Gas Prices in US from 1970-2017")
# plt.xlabel("Year")
# plt.ylabel("Price ( Dollars / Million BTU )")
# plt.scatter( x, y, c='b', label='US')
# plt.show()

# dataset_US = pd.read_csv("usa_natgas_expenditures.csv")
# x = dataset_US['Year'].values.reshape(-1, 1)
# y = dataset_US['Expenditures'].str.replace(",", "").astype(float).values.reshape(-1, 1)
# plt.title("Natural Gas Expenditures in US from 1970-2017")
# plt.xlabel("Year")
# plt.ylabel("Expenditure ( Million $ )")
# plt.scatter( x, y, c='r', label='US')
# plt.show()
