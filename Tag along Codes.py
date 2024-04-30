# -*- coding: utf-8 -*-
"""StageB.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14FiTJKLxpd6tHvsl2fRM6NLKCp44khEh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("/content/energydata_complete.csv")

data.head()

df = data.info()

#change the date column from object to datetime datatype

import pandas as pd
data['date'] = pd.to_datetime(data['date'])

data.info()

# QUESTION 17

#fit a linear model on the relationship between the temperature in the living room in Celsius (x = T2) and the temperature outside the building (y = T6). What is the Root Mean Squared error in three decimal places?

import numpy as np
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['T2'], data['T6'], test_size=0.2)

# Fit a linear regression model
model = LinearRegression()
model.fit(X_train.values.reshape(-1, 1), y_train)

# Predict the temperature in the living room based on the outside temperature
y_pred = model.predict(X_test.values.reshape(-1, 1))

# Calculate the root mean squared error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Print the root mean squared error
print(f"Root Mean Squared Error: {rmse:.3f}")

#QUESTION 18

#Remove the following columns: [“date”, “lights”]. The target variable is “Appliances”. Use a 70-30 train-test set split with a  random state of 42 (for reproducibility). Normalize the dataset using the MinMaxScaler (Hint: Use the MinMaxScaler fit_transform and transform methods on the train and test set respectively). Run a multiple linear regression using the training set. What is the Mean Absolu

# Remove the specified columns
data.drop(columns=["date", "lights"], inplace=True)

# Set the target variable
target = "Appliances"

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data.drop(target, axis=1), data[target], test_size=0.3, random_state=42
)

# Normalize the data
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Run a multiple linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_normalized, y_train)

# Calculate the mean absolute error
from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X_test_normalized)
mae = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error:", mae)

# QUESTION 19

#What is the Root Mean Squared Error (in three decimal places) for the training set?

import numpy as np
# Calculate the root mean squared error for the training set

y_train_pred = model.predict(X_train_normalized)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))

print("Root Mean Squared Error (Training Set):", rmse_train)

#QUESTION 20
#What is the Mean Absolute Error (in three decimal places) for test set?

print("Mean Absolute Error (Test Set):", mae)

#question 21
#What is the Root Mean Squared Error (in three decimal places) for test set?

import numpy as np
y_pred = model.predict(X_test_normalized)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))

print("Root Mean Squared Error (Test Set):", rmse_test)

# question 24 : Train a lasso regression model with default value and obtain the new feature weights with it. How many of the features have non-zero feature weights?

import numpy as np
# Train a Lasso regression model with default parameters
lasso_model = Lasso()
lasso_model.fit(X_train_normalized, y_train)

# Obtain the new feature weights
lasso_coef = lasso_model.coef_

# Count the number of non-zero feature weights
num_non_zero_weights = np.count_nonzero(lasso_coef)

# Print the number of non-zero feature weights
print("Number of non-zero feature weights:", num_non_zero_weights)

# question 25 : What is the new RMSE with the Lasso Regression on the test set?

import numpy as np
# Predict using the Lasso model
y_pred_lasso = lasso_model.predict(X_test_normalized)

# Calculate the Root Mean Squared Error
rmse_lasso = np.sqrt(mean_squared_error(y_test, y_pred_lasso))

# Print the Root Mean Squared Error
print("Root Mean Squared Error (Lasso Regression, Test Set):", rmse_lasso)