import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,2,3,4,5,6,7,8,9,10]
fig = plt.figure(figsize=(5,4))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
axes.scatter(x, y, color='r',label='Scatter')
axes.legend(loc=0)
# plt.grid()
plt.show()

