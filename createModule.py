#a file containing a set of functins you want to inckude in your application

#create a module

# Main script
import Module as kaku  # Importing the custom module

kaku.hablu()  # Calling the hablu function
kaku.gablu()  # Calling the gablu function
kaku.eshan()  # Calling the eshan function


#call person object from module 

print(kaku.person) 

#call using class name
from Module import hablu
hablu()