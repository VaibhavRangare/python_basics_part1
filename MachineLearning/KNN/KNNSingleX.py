import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from MergeTwoArrays import merge,mergePredictions
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x = pd.Series(np.array([1,2,3,4,5,6,7,8,9,10])).values.reshape(-1,1)  
#y = pd.Series(np.array(['dog','dog','dog','dog','Horse','Horse','Horse','Horse','Horse','Horse'])).values.reshape(-1,1).ravel()
y = pd.Series(np.array([0,0,0,0,1,1,1,1,1,1])).values.reshape(-1,1).ravel()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
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

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
#pred = knn.predict(X_test)

yy = pd.Series(np.array([4,12])).values.reshape(-1,1) 
predictions = knn.predict(yy)  
print(predictions) 

print(f'Predictions for future inputs: {np.array([11,12])}')
a3 = np.array([1,2])
b3 = np.array(["X_Future","Y_Result"])
c3 = merge(np.array([4,12]),predictions)
result_df = pd.DataFrame(index=a3,columns=b3,data=c3)
print(result_df)

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(9,4))
fig.suptitle('KNN')
#axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes[0][0].set_xlabel('Train Input')
axes[0][0].set_ylabel('Train Output')
axes[0][0].set_title('Train Results')
print(X_train)
print(y_train)
data = pd.DataFrame({"X Value": X_train.flatten(), "Y Value": y_train})
groups = data.groupby("Y Value")
for name, group in groups:
    displayvalue = ''
    if(name==0):
        displayvalue = 'Dog'
    elif(name==1):
        displayvalue = 'Horse'
    axes[0][0].plot(group["X Value"], group["Y Value"], marker="o", linestyle="", label=displayvalue)
    axes[0][0].legend()

#axes[0][0].scatter(X_train, y_train)
#plt.legend()

axes[0][1].set_xlabel('Test Input')
axes[0][1].set_ylabel('Test Output')
axes[0][1].set_title('Test Results')
data = pd.DataFrame({"X Value": X_test.flatten(), "Y Value": y_test})
groups = data.groupby("Y Value")
for name, group in groups:
    displayvalue = ''
    if(name==0):
        displayvalue = 'Dog'
    elif(name==1):
        displayvalue = 'Horse'
    axes[0][1].plot(group["X Value"], group["Y Value"], marker="o", linestyle="", label=displayvalue)
    axes[0][1].legend()
#axes[0][1].scatter(X_test,y_test)

axes[1][0].set_xlabel('Future Input')
axes[1][0].set_ylabel('Predicted Output')
axes[1][0].set_title('Prediction Results')
data = pd.DataFrame({"X Value": np.array([4,12]), "Y Value": predictions})
groups = data.groupby("Y Value")
for name, group in groups:
    displayvalue = ''
    if(name==0):
        displayvalue = 'Dog'
    elif(name==1):
        displayvalue = 'Horse'
    axes[1][0].plot(group["X Value"], group["Y Value"], marker="o", linestyle="", label=displayvalue)
    axes[1][0].legend()
#axes[1][0].scatter(np.array([4,12]),predictions)


fig.tight_layout()
plt.show()
