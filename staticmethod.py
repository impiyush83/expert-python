class Person(object):
    weight = 20

    def __init__(self, age):
        self.age = age

    @staticmethod
    def print_age():
        print("The weight is 20 ")

    @staticmethod
    def create_object(age):
        return Person(age)


person_object = Person(50)
father = person_object.create_object(60)
print(father.__dict__)
