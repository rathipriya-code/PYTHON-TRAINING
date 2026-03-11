'''
"Python Learning"
Learning: "OOPS-concept-Polymorphism"
DAY01-Task

'''

'''
COMPILE TIME POLYMORPHISM
'''
print("==================COMPILE TIME POLYMORPHISM==============")
class calculation:
    def add(self, a=1,b=2, *args):
        result = a + b
        for num in args:
            result += num
        return result
input=calculation()
print(input.add())
print()
print(input.add(1,1))
print()
print(input.add(7,7))
print()
print(input.add(10,10))
print()
print(input.add(11))
print()
print(input.add("HELLO","WORLD"))
print()
print(input.add(20,10,1,2,3))
print()


'''
RUN-TIME POLYMORPHISM
'''
print("=================RUN-TIME POLYMORPHISM====================")

class Animal:
    def display_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def display_sound(self):
        return "Bark"

class Cat(Animal):
    def display_sound(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.display_sound())