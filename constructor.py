class ParentInfo:
    def eshanfamily(self, name, age):
        print(f"My name is {name}, my age is {age}")


# Create an instance of ParentInfo
p1 = ParentInfo()

# Call the method with arguments
p1.eshanfamily("Eeshan", 19)





#parameterized constructor

class ParentInfo:
    # Parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eshanfamily(self):
        print(f"My name is {self.name}, my age is {self.age}")


# Create an instance of ParentInfo
p1 = ParentInfo("Eeshan", 19)

# Call the method
p1.eshanfamily()
