""" It allows you to hide the implementation details of a particular functionality and only expose the essential features to the use"""

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method

# Concrete class
class Dog(Animal):
    def sound(self):
        return "Bark"

# Concrete class
class Cat(Animal):
    def sound(self):
        return "Meow"

# Usage
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
