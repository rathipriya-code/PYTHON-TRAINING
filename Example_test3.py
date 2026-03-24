print("==========Inheritance=====================")

class Birds:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print("flying")
    def sleep(self):
        print("sleeping")
    def eat(self):
        print("eating")
class Hen(Birds):
    def __init__(self,pet_name):
        super().__init__("Hen")
        self.pet_name=pet_name
    def say_buk(self):
        print("Hens say buk buk")
class peacock(Birds):
    def __init__(self,pet_name):
        super().__init__("Peacock")
        self.pet_name=pet_name
    def say_may_aw(self):
        print("Peacocks say may aw")
h1=Hen("Chicku")
print(h1.pet_name)
h1.say_buk()
h1.fly()
h1.sleep()
h1.eat()
p1=peacock("Clara")
print(p1.pet_name)
p1.say_may_aw()
p1.fly()
p1.sleep()
p1.eat()
