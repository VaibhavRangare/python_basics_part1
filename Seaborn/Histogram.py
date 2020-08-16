import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../Datasets/datasets_19_420_Iris.csv')
print(df.head())
#sns.distplot(df['SepalWidthCm'],kde=False)
#sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',data=df,kind='hex')
#sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',data=df,kind='reg')
sns.pairplot(df,hue='Species')
plt.show()