class Person:
    def __init__(self, age: int = None, name: str = None):
        self.age = age
        self.name = name

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


a = Person(34, 23)
a.display_info()

b = Person()
b.name = "Ram"
b.age = 25
b.display_info()

c = Person()
c.display_info()
