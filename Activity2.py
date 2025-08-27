class Animal:
    def move(self):
        pass  # base method (to be overridden)


class Dog(Animal):
    def move(self):
        print("🐕 Running on 4 legs!")


class Bird(Animal):
    def move(self):
        print("🐦 Flying in the sky!")


class Fish(Animal):
    def move(self):
        print("🐟 Swimming in the water!")


# Demonstrate polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
