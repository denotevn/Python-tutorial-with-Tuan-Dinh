from ast import walk


class Mamal:
    def walk(self):
        print("walk!")


class Dog(Mamal):
    def bark(self):
        print("Bark")

class Cat(Mamal):
    def be_annoying(self):
        print("annoying")

cat1 = Cat()
cat1.walk()
cat1.be_annoying()

dog = Dog()
dog.walk()  # walk
