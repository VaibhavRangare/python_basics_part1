"""
List
Ordered
Indexed
Mutable
Duplicates allowed
"""

items = [1,2,3]
items = list([1,2,3])
items = [1,2,3]

items = list(range(1,11))
print(type(items))

items.clear()

items = [11,4,5,6,2,1,3,9,8,7,10]
items.sort()
items.append(12)
''' items.insert(0,123) '''

l = list()
l = map(lambda n: n*2,items)

for item in l:
    print(item)
