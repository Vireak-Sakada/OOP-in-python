class Animal: 
    def __init__(self, name):
        self.name = name 
        self.is_alive = True 
    #methot
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is asleep")
class Dog(Animal):
    def speak(self):
        print("WOFF!")
class Cat(Animal):
    def speak(self):
        print("moew")
class Mouse(Animal):
    def speak(seld):
        print("squeek")
dog = Dog("scooby")
cat = Cat("garfield")
mouse = Mouse("mickey")
# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
dog.speak()