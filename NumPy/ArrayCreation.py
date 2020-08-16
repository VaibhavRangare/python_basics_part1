import numpy as np
a = np.array([1, 3, 5, 7, 9])
print(a)
a = np.zeros(3)
print(a)
a = np.ones(3)
print(a)
a = np.linspace(1,10,5)
print(a)
a = np.arange(1,10)
print(a)
a = np.random.randint(0,10,6)
print(a)
a = a.reshape(3,2)
print(a)
print(a.min())
print(np.min(a))
print(np.argmin(a))
print(np.shape(a))



