import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6,7,8,9,10])
y = np.array([0,1,2,3,4,5,6,7,8,9,10])
counts = [x.sum(), y.sum()]
fig = plt.figure(figsize=(5,4))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
axes.pie(counts, labels=['item1', 'item2'])
axes.legend(loc=(0.1,0.9))
fig.tight_layout()
plt.show()

