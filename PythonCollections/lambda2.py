
def myFunction(l,operation):
    l1 = list()
    for i in l:
        l1.append(operation(i))
    l = l1    
    return l1

l = [1,2,3]
myFunction(l, lambda a: a*2)
l1= myFunction(l, lambda a: a*2)

print(l)
print(l1)


