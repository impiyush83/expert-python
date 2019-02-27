# super(subclass, instance).fucntion_of_parent()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        print(face_area)
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


rectangle = Rectangle(length=2, width=3)
print("Rectangle :")
print(rectangle.length)
print(rectangle.width)

print("Square :")
square = Square(5)
print(square.area())

print("Rectangle :")
print(rectangle.length)
print(rectangle.width)


print("Cube :")
cube = Cube(length=50)
cube.surface_area()
print(cube.surface_area())
