class Animal:
    def __init__(self,name):
       self.name = name
    def walk(self):
        print(f"{self.name} walks")
    

class Dog(Animal):            
    def barking(self):
        print("barks")

class Cat(Animal):   
    def sleeping(self):
        print("sleeping")

bulbul = Dog("bulbul")
bulbul.walk()
bulbul.barking()

sanju = Cat("sanju")
sanju.walk()
sanju.sleeping()
