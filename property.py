class Person(object):

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    @property
    def show_age(self):
        return self.age


person = Person(40, 50)
print(person.show_age)
