# Base class 1
class Parent1:
    def greet(self):
        print("Hello from Parent1!")

# Base class 2
class Parent2:
    def introduce(self):
        print("Hello from Parent2!")

# Child class inheriting from both Parent1 and Parent2
class Child(Parent1, Parent2):
    def display(self):
        print("I am the Child class.")

# Create an object of the Child class
child = Child()

# Access methods from both Parent1 and Parent2, as well as its own method
child.greet()        # Method from Parent1
child.introduce()    # Method from Parent2
child.display()      # Method from Child
