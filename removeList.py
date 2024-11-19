#remove item from list


#remove is used for using direct item in the list
x=["Sakib","Amin","mehedi","Sumon"]
x.remove("mehedi")
print(x)


x=["Sakib","Amin","mehedi","Sumon",420]
x.remove(420)
print(x)


#pop() is used in the list for using index
x=["Sakib","Amin","mehedi","Sumon"]
x.pop(1)
print(x)


#del is also used for deleting the specified item in the list

x=["Sakib","Amin","mehedi","Sumon"]
del x[0]
print(x)


#clear the list
print(x)
x.clear()
print(x)