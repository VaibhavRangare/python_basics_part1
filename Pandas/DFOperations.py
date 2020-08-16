import numpy as np
import pandas as pd

index = np.array([0,1,2,3,4,5,6])
columns = np.array(['Name','Age','Gender','Show'])
data = [
    ['John',10,'M','Kidzee'],
    ['Jinny',10,'F','Kidone'],
    ['Castor',11,'M','Kidkill'],
    ['Troy',12,'M','Kidkill'],
    ['Angel',9,'F','Kidmoon'],
    ['Gretel',11,'M','Kidhorror'],
    ['Elv',15,'F','Kidzee'],
]
df = pd.DataFrame(index=index, columns=columns,data=data)
print(df)
# To get only girls performance
# df = df[df['Gender']=='F']
# To get only boys performance
# df = df[df['Gender']=='M']
# To get only girls performance whose age is >10
# df = df[(df['Age']>10) & (df['Gender']=='F')]
# df = df[df['Gender']=='M'][['Name','Age']]
# To change the index
# df.set_index('Show',inplace=True)
# df = df.set_index('Show')
# print(df)