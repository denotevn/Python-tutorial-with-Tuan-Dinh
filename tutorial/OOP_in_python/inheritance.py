from ast import walk


class Mamal:
    def walk(self):
        print("walk!")


class Dog(Mamal):
    pass

class Cat(Mamal):
    pass

dog = Dog()
dog.walk()  # walk
