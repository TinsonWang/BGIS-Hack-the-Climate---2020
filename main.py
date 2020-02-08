import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('Book1.csv')

print(dataset.shape)

x = dataset['Year'].values.reshape(-1,1)
y = dataset['NatGas'].values.reshape(-1,1)

y = dataset['NatGas'].str.replace(',', "").astype(int).values.reshape(-1, 1)

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

plt.scatter(x_test, y_test, color='blue')
plt.scatter(x_test, y_pred, color='red')
plt.show()