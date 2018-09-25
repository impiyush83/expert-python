class Person(object):
    weight = 20

    def __init__(self, age):
        self.age = age

    @classmethod
    def print_age(cls):
        print("The weight is {}".format(cls.weight))

    @classmethod
    def create_object(cls, age):
        return cls(age)


person_object = Person(50)
person_object.print_age()
new_person_object = person_object.create_object(70)
print(new_person_object.__dict__)
