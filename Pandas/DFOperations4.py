import numpy as np
import pandas as pd

df = pd.read_csv('../Datasets/covid19_tweets.csv')
print(type(df))
print(df.head())
df1 = df['user_name']
print(df1)
 