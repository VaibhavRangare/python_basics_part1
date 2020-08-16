import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
from scipy.special import expit
from MergeTwoArrays import merge,mergePredictions
import json
cf.go_offline()
train = pd.read_csv('titanic_train.csv')

train.drop('Cabin',axis=1,inplace=True)

train.dropna(inplace=True)
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)
x = pd.Series(np.array([1,2,3,4,5,6,7,8,9,10])).values.reshape(-1,1)  
y = pd.Series(np.array([0,0,0,0,1,1,1,1,1,1])).values.reshape(-1,1).ravel()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

print(type(X_train))
print(type(y_train))

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

from sklearn.linear_model import LogisticRegression
lm = LogisticRegression()
lm.fit(X_train,y_train)
#predictions = lm.predict(X_test)  
yy = pd.Series(np.array([4,12])).values.reshape(-1,1) 
predictions = lm.predict(yy)  
print(predictions) 

print(len(predictions))  
#aaa = np.arange(0,len(predictions))
#print(aaa)
#print(predictions)

print(f'Predictions for future inputs: {np.array([11,12])}')
a3 = np.array([1,2])
b3 = np.array(["X_Future","Y_Result"])
c3 = merge(np.array([4,12]),predictions)
result_df = pd.DataFrame(index=a3,columns=b3,data=c3)
print(result_df)

#b = np.array(["Predict"])
#hh= pd.Series(data=predictions)
#print(hh.head())
#ff = pd.DataFrame(index=aaa,data=predictions,columns=pd.concat([X_test,hh],axis=1))
#ff = pd.concat([X_test,hh],axis=0)
#print(X_test)
#print(ff.head())
#print(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))


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
axes[1][0].scatter(np.array([4,12]),predictions)

axes[1][1].set_xlabel('X')
axes[1][1].set_ylabel('Y')
axes[1][1].set_title('Regression Line')
fitlinex = np.array([0,1,2,3,4,5,6,7,8,9,10])
loss = expit(x * lm.coef_ + lm.intercept_).ravel()
axes[1][1].plot(x,loss)


fig.tight_layout()
plt.show()
                     
