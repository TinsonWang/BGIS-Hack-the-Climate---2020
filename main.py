import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('usa_natgasc_clean.csv')

#print(dataset.shape)

# x will contain our input parameters:
#   - the (x,y) coordinates of the state with respect to our map.
#   - the year that we want to examine the natural gas consumption.
x = dataset[['X', 'Y', 'Year']].values.reshape(-1,3)

# y will contain our output parameters:
#   - the natural gas consumption for the location and year specified.
y = dataset['NatGasC'].values.reshape(-1,1)

# We use this function to clean up the values for Natural Gas Consumption because they contain commas.
y = dataset['NatGasC'].str.replace(',', "").astype(int).values.reshape(-1, 1)

# Because the range of our values for Natural Gas Consumption wildly varies, I figured we should normalize it.
y_min = y.min()
y_max = y.max()
y_normalized = np.divide( np.subtract( y, y_min), y_max-y_min )

# Split our dataset into training and test sets.
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y_normalized,
                                                    test_size=0.2,
                                                    random_state=0)

# Initialize our Machine Learning model and fit the training data.
model = LinearRegression()
model.fit(x_train, y_train)

# Assign y_pred to our predicted values from x_test values.
# The y_test values will be holding the CORRECT values.
y_pred = model.predict(x_test)

# Store our actual and predicted y values (Natural Gas Consumption) and store them into a Pandas DataFrame.
results = pd.DataFrame({'Actual': y_test.tolist(),
                        'Predicted': y_pred.tolist()})

# Uncomment the print below to see our results.
#print(results)

# Below are various error measurements printed to the screen. I have no fucking clue how to interpret it. LOL
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred) )
print('Mean Squared Error: ', metrics.mean_squared_error(y_test, y_pred) )
print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)) )

