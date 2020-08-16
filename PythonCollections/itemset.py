"""
Set
Unordered
Unindexed
Mutable
No Duplicates allowed
"""


items = 1,2,3
items = {1,2,3,3}
items = range(1,11)
items = {1,2,2,3,3}
items = set(range(1,10))
items = set([1,2,3])
print(type(items))
items.add(5)


for item in items:
    print(item)

