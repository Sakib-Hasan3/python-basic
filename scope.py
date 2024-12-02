#a variable created inside a function belongs to the local scope of thaht function. It is not

#a variable created inside a function inside that function

def x():
    y=30
    print(y) #local scope
x()
    


#global scope is written before the function  and it should be written before r afther functionand object 

a=50 #global scope
b=60


def x():
    y=30   #local scope
    print(y)
    print(a)
x()


#global keyword is used to change the variable of global scope 

a=50 #global scope
b=60


def x():
    global a #local scope
    a=100
    print(a)
x()