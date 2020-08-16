import numpy as np
import pandas as pd

a = np.array([0,1,2,3,4,5])
b = np.array(["a","b","c","d","e","f"])
print(a)
print(b)
s = pd.Series(index=a,data=b)
print(s)
print(s[0])
