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

# df = df.groupby('Show').describe().transpose()
# print(df)

# df = df['Show'].unique()
# df = df['Show'].unique()[0]
# df = df['Show'].value_counts()
# df = df['Show'].apply(lambda var: var+"_Show")
# df = df.columns
# df = df.columns[0]
df = df.sort_values('Age')
print(df)
 