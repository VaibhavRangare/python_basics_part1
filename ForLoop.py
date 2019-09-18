from builtins import print

for item in 'Python':
    print(item)
for item in [1, 2, 3, 4]:
    print(item)
for item in ['One', 'Two', 'Three']:
    print(item)
for item in range(10):                          # 1 to 10-1
    print(item)
for item in range(5, 10):                        # 5 to 10
    print(item)
for item in range(5, 10, 2):                      # 5 to 10-1 step by 2
    print(item)
items = [1, 2, 3, 4]
sum = 0
for i in items:
    sum = sum + i
print(i)

numbers = [5, 2, 5, 2, 2]
for items in numbers:
    print('*'*items)
