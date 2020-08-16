import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

men_means = (20, 35, 30, 35, 27)
print(type(men_means))
dict1 = {
    "cement": [200, 400, 600, 800, 1000],
    "strength": [240, 340, 440, 540, 640],
}

values = pd.DataFrame(dict1)
x = values[['cement']]
y = values[['strength']]
print(type(x))
independent_variable = np.array(x['cement'])
dependent_variable = np.array(y['strength'])
print(type(dependent_variable))
print(independent_variable)
print(dependent_variable)
independent_variable_pos = [i for i, _ in enumerate(independent_variable)]
plt.figure()
# plt.grid()
plt.bar(independent_variable_pos, dependent_variable, label="Example one", color='green')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.legend(loc='upper left')
plt.xticks(independent_variable_pos, independent_variable)
plt.show()
