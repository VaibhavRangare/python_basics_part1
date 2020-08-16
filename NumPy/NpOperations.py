import numpy as np
a = np.arange(1,10)
b = np.arange(1,10)
a = a + b
print(a)
a = a * 2
print(a)
c = a
c = c[c>5]
c = c>5
print("***")
print(c)

c = np.sin(a)
print(c)
c = np.sqrt(a)
print(c)

c = a>5
print(c)
