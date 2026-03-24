'''
"Python Learning"
Learning: " ABSTRACTION -- oops concept "

Example: " Simple example- Python Abstraction Example using ABC and @abstractmethod "

'''

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self): # here we hiding the unncessary details and showing only the necessary details to the user.
        pass


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


d = Dog()
d.make_sound()

c = Cat()
c.make_sound()

'''

Another Example- "Mathematical Formulas & their calculation of particular shapes"


'''


from abc import ABC, abstractmethod


class Shapes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shapes):
    def area(self, sides):
        self.sides = sides
        Area = sides * sides
        return Area

    def perimeter(self, sides):
        self.sides = sides
        Perimeter = 4 * sides
        return Perimeter


class Rectangle(Shapes):
    def area(self, length, base):
        self.length = length
        self.base = base
        Area = length * base
        return Area

    def perimeter(self, length, base):
        self.length = length
        self.base = base
        Perimeter = 2 * (length + base)
        return Perimeter


class Parallelogram(Shapes):
    def area(self, base, height):
        self.base = base
        self.height = height
        area = base * height
        return area

    def perimeter(self, sides, base):
        self.sides = sides
        self.base = base
        perimeter = 2 * (sides + base)
        return perimeter


s1 = Square()
print("Area of square is:", s1.area(10))
print("Perimeter of square is:", s1.perimeter(10))

r1 = Rectangle()
print("Area of Rectangle is:", r1.area(10, 20))
print("Perimeter of Rectangle is:", r1.perimeter(10, 20))

p1 = Parallelogram()
print("Area of Parallelogram is:", p1.area(10, 20))
print("Perimeter of Parallelogram is:", p1.perimeter(10, 20))
         