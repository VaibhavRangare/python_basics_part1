import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from MergeTwoArrays import merge,mergePredictions
import json

df = pd.read_csv('USA_Housing.csv')
x = pd.Series(np.array([1,2,3,4,5,6,7,8,9,10])).values.reshape(-1,1)  
y = pd.Series(np.array([2,3,4,5,6,7,8,9,10,11])).values.reshape(-1,1) 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)
a1 = np.array([1,2,3,4,5,6,7,8])
b1 = np.array(["X_Train","Y_Train"])
c1 = merge(X_train,y_train)
train_df = pd.DataFrame(index=a1,columns=b1,data=c1)
a2 = np.array([1,2])
b2 = np.array(["X_Test","Y_Test"])
c2 = merge(X_test,y_test)
test_df = pd.DataFrame(index=a2,columns=b2,data=c2)
print(len(train_df.index))
print(train_df)
print(test_df)

lm = LinearRegression()


lm.fit(X_train,y_train)
print(f'Fit line equation is y = m*x + c')
print(f'Fit line equation is y = {lm.coef_}*x + {lm.intercept_}')
print(f'Where m is: {lm.coef_}')
print(f'And c is: {lm.intercept_}')

#predictions = lm.predict(X_test)
yy = pd.Series(np.array([11,12])).values.reshape(-1,1) 
predictions = lm.predict(yy)
#print(f'Predictions: {type(predictions)}')
#print(predictions)
print(f'Predictions for future inputs: {np.array([11,12])}')
a3 = np.array([1,2])
b3 = np.array(["X_Future","Y_Result"])
c3 = mergePredictions(np.array([11,12]),predictions)
result_df = pd.DataFrame(index=a3,columns=b3,data=c3)
#print(result_df)
#result_df1 = pd.concat(np.array([11,12]),predictions)
#print(result_df1)
#print(c3[0])
st = "["
for i in c3:
    #print(i)
    st = st+json.dumps({'input':i[0],'output':i[1]})
    st =st+","
    #st = st+json.dumps({'output':i[1]})
st =st+"]"
print(st)

#row_json = json.dumps(c3)
#print(row_json)

#plt.scatter(y_test,predictions)
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(9,4))
#axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes[0][0].set_xlabel('Train Input')
axes[0][0].set_ylabel('Train Output')
axes[0][0].set_title('Train Results')
axes[0][0].scatter(X_train,y_train)

axes[0][1].set_xlabel('Test Input')
axes[0][1].set_ylabel('Test Output')
axes[0][1].set_title('Test Results')
axes[0][1].scatter(X_test,y_test)

axes[1][0].set_xlabel('Future Input')
axes[1][0].set_ylabel('Predicted Output')
axes[1][0].set_title('Prediction Results')
axes[1][0].scatter(np.array([11,12]),predictions)

axes[1][1].set_xlabel('X')
axes[1][1].set_ylabel('Y')
axes[1][1].set_title('Fit Line')
fitlinex = np.array([0,1,2,3,4,5,6,7,8,9,10])
axes[1][1].plot(x,lm.coef_*x+lm.intercept_)

#axes.plot(X_train,lm.coef_*X_train+lm.intercept_)
#plt.scatter(X_test,y_test)
fig.tight_layout()
plt.show()
#plt.plot(X_train,lm.coef_*X_train+lm.intercept_)
#plt.show()
# sns.distplot((y_test-predictions),bins=50)

#plt.show()
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
