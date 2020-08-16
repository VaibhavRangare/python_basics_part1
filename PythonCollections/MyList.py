class MyList(list):
    def __init__(self,list1):
        self.list1 = list1

    def forEach(self,println):
        for i in self.list1:
            #print(i)
            println(i)

    def MyListMap(self,func):
        l1 = list()
        for i in self.list1:
            l1.append(func(i))
        #print(l1)    
        self.list1 = l1    

    def MyFilter(self,func):
        l1 = list()
        for i in self.list1:
            if(func(i)):
                l1.append(i)
        #print(l1)    
        self.list1 = l1    
        
        
    def __str__(self):
        str1 = f'{self.list1}'
        return str1



l = list([1,2,3])
l = list(['Johnnnyyyyy','castor','troy'])
li = MyList(l)
#print(l.list1)
#li.forEach(lambda var: print(var))
#li.MyListMap(lambda var: var+"Hero")
#li.MyFilter(lambda var: len(var)>12)
#print(li)