from pydoc_data.topics import topics
from unicodedata import name


class Person:
    def __init__(self, name, age, topics) -> None:
        self.name = name
        self.age = age
        self.topics = topics
    def talk(self):
        print(f"Hi! I am {self.name}.\nI'm {self.age} years old.")
        print(f"{self.name} talk to you about some {self.topics}")


person = Person(name = "Tuan Dinh", age = 25, topics="topics")
person.talk()