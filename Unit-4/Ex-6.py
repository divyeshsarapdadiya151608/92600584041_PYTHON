
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Method overriding and polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()