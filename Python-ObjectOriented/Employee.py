class Employee:
    def __init__(self, type, country):
        self.type = type
        self.country = country

    def getType(self):
        return f'Employee is: {self.type}'
    
    def getCountry(self):
        return f'Employee country is: {self.type}'

class Manager(Employee):
    def __init__(self,name,age, gender):
        Employee.__init__(self,"Manager","US")
        self.name = name
        self.age = age
        self.gender = gender

    def reportTo(self):
        print(f'{self.name} reports to his manager')
