def operation(x):
    l = list()
    for i in x:
        print(i)
        i*2
        l.append(i*2)
    return l

def myFunction(l):
    l1 = operation(l)
    return l1

l = [1,2,3]
l1 = myFunction(l)
print(l1)


