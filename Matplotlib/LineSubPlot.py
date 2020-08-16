import matplotlib.pyplot as plt
import numpy as np

x0 = np.linspace(0,10)
y0 = np.sin(x0)
x1 = np.linspace(0,10)
y1 = np.linspace(0,10)
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,3))
axes[0].set_xlabel('X0 Label')
axes[0].set_ylabel('Y0 Label')
axes[0].set_title('Title0')
axes[1].set_xlabel('X1 Label')
axes[1].set_ylabel('Y1 Label')
axes[1].set_title('Title1')
axes[0].plot(x0,y0)

axes[1].plot(x1,y1)

plt.show()