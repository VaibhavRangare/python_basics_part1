class Animal:
    def __set__(self, instance, value):
        pass

    def walk(self):
        print(self)
        print("Walking")


class Dog(Animal):
    def __init__(self):
        self.name = "John"          # name = "John" will not work, need to use self.name


    def dog_walk(self):             # pass self as argument, dog_walk() not work
        print("Dog Walking")


dog = Dog()                     # () are required
print(dog.name)
dog.dog_walk()
dog.walk()
