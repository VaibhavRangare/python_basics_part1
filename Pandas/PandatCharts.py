import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Datasets/datasets_19_420_Iris.csv')
df2 = df.head()
print(df2)
# Histogram
# df['PetalLengthCm'].hist()
# df['PetalLengthCm'].plot(kind='hist')
# df[['PetalLengthCm','SepalWidthCm']].plot(kind='hist',alpha=0.5)
# Area 
# df[['PetalLengthCm','SepalWidthCm']].plot(kind='area',alpha=0.5)
# Bar
# df2[['PetalLengthCm','SepalWidthCm']].plot(kind='bar',alpha=0.5)
# Line
# df2.plot(kind='line',x='SepalLengthCm',y='PetalLengthCm',alpha=0.5)
# Scatter
# df2.plot(kind='scatter',x='SepalLengthCm',y='PetalLengthCm',c='SepalWidthCm',alpha=0.5,cmap='coolwarm')
# df2.plot.scatter(x='SepalLengthCm',y='PetalLengthCm',c='SepalWidthCm',alpha=0.5,cmap='coolwarm')
df2.plot(kind='scatter',x='SepalLengthCm',y='PetalLengthCm',s=df2['SepalWidthCm']*100)
plt.show()