import numpy as np

a = np.array([5,2,3,4,5])
b = np.array([1,2,3,4,5])
c = np.array([5,2])
d = [[12],[13]]


def merge(list1, list2):
    a1 = (len(list1),2)
    arr = np.zeros(a1)
    for index in enumerate(list1):
        arr[index[0]][0] = list1[index[0]]
        arr[index[0]][1] = list2[index[0]]
    return arr

def mergePredictions(list1, list2):
    a1 = (len(list1),2)
    arr = np.zeros(a1)
    for index in enumerate(list1):
        arr[index[0]][0] = list1[index[0]]
        arr[index[0]][1] = list2[index[0]][0]
    return arr
# a1 = merge(a,b)
# a2 = mergePredictions(c,d)
#print(a2)


