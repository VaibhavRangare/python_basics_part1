import numpy as np
import pandas as pd

index = np.array([0,1,2,3,4,5,6,7,8])
columns = np.array(['Name','Age','Gender','Show'])
data = [
    ['John',10,'M','Holloween'],
    ['Jinny',10,'F','Wondreland'],
    ['Castor',11,'M','Holloween'],
    ['Troy',12,'M','Wondreland'],
    ['Angel',9,'F','Holloween'],
    ['Frodo',11,'M','Lord Of The Rings'],
    ['Elv',15,'F','Lord Of The Rings'],
    ['Gandalf',11,'M','Lord Of The Rings'],
    ['Sam',11,'M','Lord Of The Rings'],
]
df = pd.DataFrame(index=index, columns=columns,data=data)
# To drop a row with NaN values
# df = df.dropna(axis=0)
# To drop a columns with NaN values
# df = df.dropna(axis=1)
# To fill any missing value
# df = df.fillna(value='F')
# df = df.groupby('Show')

# print(type(df.mean()))
# print(df.mean())
# print(type(df.sum()))
# df = df.sum().loc['Holloween']
# df = df.groupby('Show').sum()
df = df.groupby('Show').describe().transpose()
print(df)
# 