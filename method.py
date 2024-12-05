class ClassName:
    # Instance method
    def instance_method(self):
        print("Hello, Python!")

    # Class method
    @classmethod
    def class_method(cls):
        print("Hello from the class method!")
    
    @staticmethod
    def staticmethod():
        print("this is static")

# Create an instance of the class
v = ClassName()

# Call the instance method
v.instance_method()
v.staticmethod()

# Call the class method
ClassName.class_method()
