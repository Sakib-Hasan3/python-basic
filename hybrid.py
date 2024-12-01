#*Hybrid inheritance is a blend of multiple inheritance types. In Python, the supported types of inheritance are single, multiple, multilevel, hierarchical, and hybrid. In hybrid inheritance, classes are derived from more than one base class, creating a complex inheritance structure.*#

# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class 1 (inherits from Animal)
class Mammal(Animal):
    def feature(self):
        print("Mammal gives birth to live young")

# Derived class 2 (inherits from Animal)
class Bird(Animal):
    def feature(self):
        print("Bird lays eggs")

# Derived class 3 (inherits from Mammal and Bird)
class Bat(Mammal, Bird):
    def bat_feature(self):
        print("Bat is a flying mammal")

# Create an object of Bat class
bat = Bat()

# Access methods from the base classes
bat.speak()          # From Animal
bat.feature()        # From Mammal (Mammal takes precedence due to MRO)
bat.bat_feature()    # From Bat
