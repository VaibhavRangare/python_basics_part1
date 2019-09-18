set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
print(set1)
# print(set1[0])                  # will not work in set
# print(set1[0:3])                # will not work in set
set3 = set1 & set2
print(set3)
set3 = set1 | set2
print(set3)
set3 = set1 ^ set2
print(set3)
set1.add(7)
print(set1)
set1.remove(5)
print(set1)
# set1.pop(2)
print(set1)
print(set1.intersection(set2))
set1.update(set2)
print(set1)
