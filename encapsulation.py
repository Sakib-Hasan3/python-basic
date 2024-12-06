""" involves bundling data (attributes) and methods that operate on the data into a single unit (a class)."""

class Vehicle:
    def __init__(self, model, brand, document):
        self.__model = model        # Private attribute
        self.__brand = brand        # Private attribute
        self.__document = document  # Private attribute

    # Getter methods
    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand

    def get_document(self):
        return self.__document

# Subclasses
class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass

# Create instances
p1 = Plane("hablu420", "hablu", "all components")
c1 = Car("bmw", "e221", "main component")

# Access attributes using getters
print(f"Plane - Model: {p1.get_model()}, Brand: {p1.get_brand()}, Document: {p1.get_document()}")
print(f"Car - Brand: {c1.get_brand()}")
