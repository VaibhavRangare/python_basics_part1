import numpy as np
import pandas as pd

index = np.array([0,1,2,3,4,5,6,7,8])
columns = np.array(['Name','Age','Gender','Show','Key'])
data1 = [
    ['John',10,'M','Holloween','k0'],
    ['Jinny',10,'F','Wondreland','k1'],
    ['Castor',11,'M','Holloween','k2'],
    ['Troy',12,'M','Wondreland','k3'],
    ['Angel',9,'F','Holloween','k4'],
    ['Frodo',11,'M','Lord Of The Rings','k5'],
    ['Elv',15,'F','Lord Of The Rings','k6'],
    ['Gandalf',11,'M','Lord Of The Rings','k7'],
    ['Sam',11,'M','Lord Of The Rings','k8'],
]
data2 = [
    ['John',10,'M','Holloween','k0'],
    ['Wizard',10,'F','Wondreland','k1'],
    ['Gimli',11,'M','Holloween','k2'],
    ['Troy',12,'M','Wondreland','k3'],
    ['Hector',9,'F','Holloween','k4'],
    ['Hansel',11,'M','Lord Of The Rings','k5'],
    ['Elv',15,'F','Lord Of The Rings','k6'],
    ['Gandalf',11,'M','Lord Of The Rings','k7'],
    ['Sam',11,'M','Lord Of The Rings','k8'],
]
df1 = pd.DataFrame(index=index,columns=columns,data=data1)
df2 = pd.DataFrame(index=index,columns=columns,data=data2)
#print(df1)
#df = pd.concat([df1,df2])
# df = pd.concat([df1,df2],axis=1)
#print(df)
df = pd.merge(df1,df2,how='inner',on='Name')
print(df)