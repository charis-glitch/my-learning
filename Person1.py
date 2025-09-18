class Person:
    def __init__(self, name):
       self.name = name

    def talk(self):
        print(f"hi, i am {self.name}")


john = Person("John")
print(john.name)
john.talk()
