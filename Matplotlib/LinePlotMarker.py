import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,6,15)
y = np.sin(x)
fig = plt.figure(figsize=(5,4))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
axes.plot(x, y, label='line1',color='red',alpha=0.5,linewidth=3,
                linestyle='--',marker='+',
                markersize=10, markerfacecolor='yellow',
                markeredgewidth=3, markeredgecolor='green' )
axes.legend(loc=0)# plt.grid()
plt.grid()
plt.show()
