class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        print(f'nameee:{self.name}')
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return f'{self.name} is aa {self.species}'

class Dog(Animal):

    def __init__(self, name1, age):
        Animal.__init__(self, "abcd", "Dog")
        self.age = age
        self.name1=name1

    def getAge(self):
        return self.age
    
    
'''
polly = Animal("Polly", "Parrot")
polly.getName()
print(polly)
'''
dog = Dog("goofy",22)
''' dog.getAge '''
print(dog.getAge())
print(dog.name1)
print(dog.name)
print(dog.species)