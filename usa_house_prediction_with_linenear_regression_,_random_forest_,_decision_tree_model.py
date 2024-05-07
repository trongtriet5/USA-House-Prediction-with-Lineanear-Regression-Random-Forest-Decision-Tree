# -*- coding: utf-8 -*-
"""[Khai thác dữ liệu và ứng dụng] House Prediction with Linenear Regression , Random Forest , Decision Tree Model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ULHi-ZdB3jKJG9BXJhL-ZzI8k0o_HQ9D
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

# %matplotlib inline

HouseDF = pd.read_csv('./USA_Housing.csv')
HouseDF.dropna(inplace=True)

x = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
y = HouseDF['Price']  # Extracting target variable directly as a Series

print("Số lượng dữ liệu sau khi xử lý bác bỏ:", len(HouseDF))

HouseDF.info()
HouseDF.describe()

# Phân tích đa biến
sns.pairplot(HouseDF)
plt.show()

# Phân tích đơn biến
plt.figure(figsize=(12, 8))
for i, column in enumerate(x.columns, 1):
    plt.subplot(2, 3, i)
    sns.histplot(x[column], kde=True)
    plt.title(f'Distribution of {column}')
plt.tight_layout()
plt.show()

# Phân tích tương quan.
plt.figure(figsize=(10, 8))
sns.heatmap(HouseDF.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

sns.histplot(HouseDF['Price'])

plt.figure(figsize=(15, 10))
for i, column in enumerate(x.columns, 1):
    plt.subplot(2, 3, i)
    sns.regplot(x=x[column], y=y, scatter_kws={'s': 10})
    plt.title(f'Reg-plot for {column} vs Price')

plt.tight_layout()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Linear Regression
lm = LinearRegression()
lm.fit(x_train, y_train)
lm_predictions = lm.predict(x_test)
plt.scatter(y_test,lm_predictions)
lm_coefficients = lm.coef_

print("Linear Regression Metrics:")
print('MAE:', metrics.mean_absolute_error(y_test, lm_predictions))
print('MSE:', metrics.mean_squared_error(y_test, lm_predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, lm_predictions)))
print("Linear Regression Metrics:")
print('Coefficients:')
for i, column in enumerate(x.columns):
    print(f'{column}: {lm_coefficients[i]}')

# Decision Tree
dt_regressor = DecisionTreeRegressor(random_state=42)
dt_regressor.fit(x_train, y_train)
dt_predictions = dt_regressor.predict(x_test)
plt.scatter(y_test,dt_predictions)
dt_feature_importances = dt_regressor.feature_importances_

print("\nDecision Tree Metrics:")
print('MAE:', metrics.mean_absolute_error(y_test, dt_predictions))
print('MSE:', metrics.mean_squared_error(y_test, dt_predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, dt_predictions)))
print('Feature Importances:')
for i, column in enumerate(x.columns):
    print(f'{column}: {dt_feature_importances[i]}')

# Random Forest
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(x_train, y_train)
rf_predictions = rf_regressor.predict(x_test)
plt.scatter(y_test,rf_predictions)
rf_feature_importances = rf_regressor.feature_importances_

print("\nRandom Forest Metrics:")
print('MAE:', metrics.mean_absolute_error(y_test, rf_predictions))
print('MSE:', metrics.mean_squared_error(y_test, rf_predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, rf_predictions)))
print('Feature Importances:')
for i, column in enumerate(x.columns):
    print(f'{column}: {rf_feature_importances[i]}')