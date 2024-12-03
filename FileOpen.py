# Create a file and write some content to test
with open("txt.txt", "w") as file:
    file.write("This is a test file.\n")

# "r" for read mode
file = open("txt.txt", "r")
print("Reading in 'r' mode:")
print(file.read())
file.close()

# "w" for write mode (clears content)
file = open("txt.txt", "w")
file.write("New content written in 'w' mode.\n")
file.close()

# "a" for append mode (appends content)
file = open("txt.txt", "a")
file.write("Appending this line in 'a' mode.\n")
file.close()

# "r+" for read and write mode
file = open("txt.txt", "r+")
print("Reading in 'r+' mode:")
print(file.read())
file.write("Adding a line in 'r+' mode.\n")
file.close()

# "w+" for write and read mode
file = open("txt.txt", "w+")
file.write("Writing and then reading in 'w+' mode.\n")
file.seek(0)  # Move to the start of the file for reading
print("Reading in 'w+' mode:")
print(file.read())
file.close()

# "a+" for append and read mode
file = open("txt.txt", "a+")
file.write("Appending and then reading in 'a+' mode.\n")
file.seek(0)  # Move to the start of the file for reading
print("Reading in 'a+' mode:")
print(file.read())
file.close()

# "x" for exclusive creation mode
try:
    file = open("txt.txt", "x")  # Will raise FileExistsError if file exists
    file.write("This file is created in 'x' mode.\n")
    file.close()
except FileExistsError:
    print("'x' mode: File already exists.")
