import numpy as np
import pandas as pd

index = np.array([0,1,2,3,4,5,6])
columns = np.array(['Name','Age','Gender','Show'])
data = [
    ['John',10,'M','Kidzee'],
    ['Jinny',10,np.nan,'Kidone'],
    ['Castor',11,'M','Kidkill'],
    ['Troy',12,'M','Kidkill'],
    ['Angel',9,'F','Kidmoon'],
    ['Gretel',11,'M','Kidhorror'],
    ['Elv',15,'F','Kidzee'],
]
df = pd.DataFrame(index=index, columns=columns,data=data)
# To drop a row with NaN values
# df = df.dropna(axis=0)
# To drop a columns with NaN values
# df = df.dropna(axis=1)
# To fill any missing value
# df = df.fillna(value='F')
# print(df)
# To apply some change in each in the df
df = df[['Name','Show']].apply(lambda var : var+"AA")
print(df)

