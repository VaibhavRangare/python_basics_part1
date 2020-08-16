import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
cf.go_offline()
train = pd.read_csv('titanic_train.csv')

#print(train.head())
#sns.countplot(x='Survived',data=train,palette='RdBu_r')
#train['Age'].hist(bins=30,color='darkred',alpha=0.7)
#train['Fare'].iplot(kind='hist',bins=30,color='green')
#plt.show()

#print(train.describe())
#print(train.info())
#print(train.columns)
#print(train['Cabin'])
#print(train.head())
train.drop('Cabin',axis=1,inplace=True)

train.dropna(inplace=True)
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)
#print(sex)
#print(train.head())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1), 
                                                    train['Survived'], test_size=0.30, 
                                                    random_state=101)

aa = pd.concat([X_train,y_train],axis=1)
print(type(X_train))
print(type(y_train))
print(y_train.head())

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)   
#print(predictions) 
print(len(predictions))  
aaa = np.arange(0,len(predictions))
#print(aaa)
#print(predictions)
b = np.array(["Predict"])
hh= pd.Series(data=predictions)
print(hh.head())
#ff = pd.DataFrame(index=aaa,data=predictions,columns=pd.concat([X_test,hh],axis=1))
ff = pd.concat([X_test,hh],axis=0)
#print(X_test)
print(ff.head())
#print(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
                                            
