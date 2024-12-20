"""It means "many forms" and allows objects of different classes to be treated as objects of a common superclass."""

# Base class
class Vehicle:
    def __init__(self, model, brand, document):
        self.model = model
        self.brand = brand
        self.document = document

# Subclass inheriting from Vehicle
class Plane(Vehicle):
    pass

class car(Vehicle):
    pass

# Create an instance of Plane
p1 = Plane("hablu420", "hablu", "all components")
c1 =car("bmw","e221","main component")

# Access and print the brand attribute
print(p1.model,p1.brand,p1.document)
print(c1.brand)
