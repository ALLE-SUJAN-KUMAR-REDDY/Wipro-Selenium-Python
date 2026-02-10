# Lab 2: Polymorphism Using Function Arguments
# Create classes Dog, Cat, and Cow each with a method speak().

class Dog:
    def speak(self):
        return "Dog says: Woof"


class Cat:
    def speak(self):
        return "Cat says: Meow"


class Cow:
    def speak(self):
        return "Cow says: Moo"


# Write a function animal_sound(obj) that calls speak().

def animal_sound(obj):
    print(obj.speak())


# Pass different objects to the same function.

d = Dog()
c = Cat()
cw = Cow()

animal_sound(d)
animal_sound(c)
animal_sound(cw)

