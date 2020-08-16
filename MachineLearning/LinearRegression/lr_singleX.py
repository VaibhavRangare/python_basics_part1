import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USA_Housing.csv')
x = df['Avg. Area Income'].values.reshape(-1,1)     
y = df['Price'].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

'''
print(type(X_train))
print(type(X_test))
print(type(y_train))
print(type(y_test))
print(X_train.head())
'''

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train,y_train)

print(lm.intercept_)
print(lm.coef_)
predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
plt.show()
# sns.distplot((y_test-predictions),bins=50)
# plt.show()
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))