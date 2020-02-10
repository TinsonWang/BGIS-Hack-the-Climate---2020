# 9 February 2020
#
# Basic Machine Learning script using sklearn's LinearRegression() model.
#
# Datasets used was obtained from the USA Energy Information Administration (EIA)
#     and was formatted by us.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("csv/usa_natgasc_clean.csv")

dataset_CA = dataset.loc[ (dataset['State'] == 'CA' ) ]
x = dataset_CA[['X', 'Y', 'Year']].values.reshape(-1, 3)
y = dataset_CA['NatGasC'].str.replace(",", "").astype(int).values.reshape(-1, 1)

# dataset_US = pd.read_csv("csv/usa_natgas_prices.csv")
# x = dataset_US['Year'].values.reshape(-1, 1)
# y = dataset_US['Prices'].values.reshape(-1, 1)

# dataset_US = pd.read_csv("csv/usa_natgas_expenditures.csv")
# x = dataset_US['Year'].values.reshape(-1, 1)
# y = dataset_US['Expenditures'].str.replace(",", "").values.reshape(-1, 1)

# Split our dataset into training and test sets.
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)

# Initialize our Machine Learning model and fit the training data.
model = LinearRegression()
model.fit(x_train, y_train)

# Assign y_pred to our predicted values from x_test values.
# The y_test values will be holding the CORRECT values.
y_pred = model.predict(x_test)

# Store our actual and predicted y values (Natural Gas Consumption) and store them into a Pandas DataFrame.
results = pd.DataFrame({'Year': x_test[:,2].tolist(),
                        'Actual Consumption (Billion BTU)': y_test.tolist(),
                        'Predicted Consumption (Billion BTU)': y_pred.tolist()}).sort_values(by=['Year'], ascending=True)

# Uncomment the print below to see our results.
print("Machine Learning Model Results: ")
print(results)

# plt.title("Natural Gas Consumption in California 1960-2017")
# plt.xlabel("Year")
# plt.ylabel("Natural Gas Consumption ( Billion BTU )")
# plt.scatter( x_test[:,2], y_pred, label='Predicted')
# plt.scatter( x_test[:,2], y_test, label="Actual")
# plt.legend()
# plt.show()

# Below are various error measurements printed to the screen.
# print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred) )
# print('Mean Squared Error: ', metrics.mean_squared_error(y_test, y_pred) )
# print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)) )
# print('R^2: ', model.score(x_test, y_test) )
