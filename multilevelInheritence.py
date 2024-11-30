class Baba:
    car = "BMW"
    tk = "100"
    home = "10 floor"
    
class Son1(Baba):
    smartphone = "iPhone"
    ac = "Walton"
    microphone = "Fifine"

class Son2(Son1):
    webcam = "Fifine K0"
    laptop = "Lenovo"
    camera = "Fifine"

class Son3(Son2):
    pass  # `pass` is used here to indicate no additional attributes or methods

# Creating an instance of Son3
k = Son3()

# Accessing an attribute from the inherited hierarchy
print(k.webcam)
