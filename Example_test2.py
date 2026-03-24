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

from abc import ABC,abstractmethod
class Remote(ABC):
    def __init__(self):
	     pass
	@abstractmethod 
	def get_battery_status(self):
	    pass
class Tv_remote(Remote):
    def get_volume_status(self):
	    print("Volume is too high on tv")
    def get_battery_status(self):
	    print("Battery level is going to die")
	
class Ac_remote(Remote):
    def get_battery_status(self):
	    print("Battery level is moderate")
	def get_temp_status(self):
	    print("Temperature level is too high, need to sets down")
	def get_mode_status(self):
	    print("It is in fan mode")
	def get_cooling_status(self):
	    print("it is too cool") 
		
class DVD_remote(Remote):
    def get_audio_status(self):
	    print("Audio is too clear")
	def get_video_status(self):
	    print("video is running")