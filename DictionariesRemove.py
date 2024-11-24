# Dictionary with initial data
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Remove a specific item using pop()
x.pop("age")
print("After removing 'age':", x)

# Delete the entire dictionary using del
del x

# If you try to print x here, it will raise an error because x no longer exists.
# Uncommenting the line below will result in a NameError:
# print(x)

# To demonstrate clearing a dictionary, recreate it first
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Clear all items from the dictionary
x.clear()
print("After clearing the dictionary:", x)
