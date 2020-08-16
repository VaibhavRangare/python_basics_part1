import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../Datasets/datasets_19_420_Iris.csv')
print(df.head())
sns.distplot(df['SepalWidthCm'])
plt.show()