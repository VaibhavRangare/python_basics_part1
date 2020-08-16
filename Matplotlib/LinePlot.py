import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)

print(x)
y = np.sin(x)
#y1 = np.linspace(0, 10,2)
y1 = np.linspace(0,10)
fig = plt.figure(figsize=(5,4))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
#plt.xticks([0,1,2,3,4,5,6,7,8,9])
#plt.yticks([-1,0,1])
axes.plot(x, y, label='line1',color='red',alpha=0.5,linewidth=3,linestyle='--')
axes.plot(x, y1,label='line2',marker='*')
axes.legend(loc=0)
# axes.grid()
# fig.savefig("test.png")
plt.show()
