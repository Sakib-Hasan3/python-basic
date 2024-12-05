#Class: A blueprint for creating objects. It defines properties (attributes) and behaviors (methods).
#Object: An instance of a class. It represents a specific example of the class."""

# Define a class

class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method to display details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to update the age
    def update_age(self, new_age):
        self.age = new_age

# Create an object (instance of the class)
person1 = Person("John Doe", 25)

# Access attributes
print(person1.name)  # Output: John Doe
print(person1.age)   # Output: 25

# Call methods
person1.display_info()  # Output: Name: John Doe, Age: 25

# Update the age
person1.update_age(30)
person1.display_info()  # Output: Name: John Doe, Age: 30
