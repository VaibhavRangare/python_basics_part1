list1 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
print(len(list1))
print(list1[0])
print(list1)
# start index:end index:step
print(list1[::2])
print(list1[:])
list1.append(9)
print(list1)
print(list1.count(8))                   # how many times an item is there in the list
print(list1.index(4))                   # index position of an item
list1.insert(3, 3)                     # insert an item at index
list1.pop(0)                            # remove element at index
list1.remove(4)                         # removes object
list1.reverse()
list1.sort()
print(list1)
list2 = [10, 11, 12]
list3 = list1 + list2
print(list3)
list1.clear()                           # empty the list
print(list1)
coordinates = [1, 2, 3]
x, y, z = coordinates                     # unpacking
print(x)
print(y)
print(z)
