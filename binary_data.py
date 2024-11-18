#binary data type

#byte is immutable or number not changeable valued

habluList = [1, 2, 45, 56, 76, 54]  # List of binary data type

# Convert the list to an immutable bytes object
b = bytes(habluList)

# Print the bytes object
print(b)

# Print the type of the object
print(type(b))





#bytearray is immutable or number can change
habluList = [1, 2, 45, 56, 76, 54]  # List of binary data type

# Convert the list to bytearray
b1 = bytearray(habluList)

# Modify an element of the bytearray
b1[1] = 10
print(b1)  # Output will be: bytearray([1, 10, 45, 56, 76, 54])

# Correct the error: print b1[1], not b[1]
print(b1[1])  # Output will be: 10 (since you changed the second element to 10)

# Printing the type of the bytearray
print(type(b1))  # Output will be: <class 'bytearray'>
