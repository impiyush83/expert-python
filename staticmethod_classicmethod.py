class Door:
    colour = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    # cant be called by class, buy can be called by object has self.
    def open(self):
        self.status = 'open'

    # does not have self and cls, can be called by class as well as method
    @staticmethod
    def close():
        # cant access object
        # explicitaly passing of objects necessary
        print("IN static method")
        status = 'closed'

    # does not have self but has cls, can be called by class as well as method.
    @classmethod
    def class_method_1(cls):
        print("IN class method")
        status = 'closed'


door1 = Door(1, 'closed')
door2 = Door(1, 'closed')
# color brown is shared among all instances of Door.
# if its changed it is changed among all instances

# will print brown
print(door1.colour)
print(door2.colour)

Door.colour = "black"

# will print black
print(door1.colour)
print(door2.colour)

# to call non-static and non-class method
door1.open()  # by_object
Door.open(door1)  # by_class

# static method call
door1.close()
Door.close()

# class method call
door1.class_method_1()
Door.class_method_1()


