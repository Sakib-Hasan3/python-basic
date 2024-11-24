#Acessing Items

student = {
    "name": "Eshan",
    "age": 18,
    "location": "Rajshahi",
    "subject": "Commerce"
}

print(student["name"])  # Output: Eshan
print(student["age"])   # Output: 18

#another way 

print(student.get("location"))  # Output: Rajshahi
print(student.get("roll"))      # Output: None (key doesn't exist)


#another way
print(student.get("roll", "Not Available"))  # Output: Not Available


#anther way

for key in student:
    print(key, ":", student[key])

#another way

if "name" in student:
    print("Name exists")
else:
    print("Name does not exist")

#another way 

nested_student = {
    "Eshan": {
        "location": "Rajshahi",
        "age": 18,
        "subject": "Commerce"
    },
    "Arya": {
        "location": "Dhaka",
        "age": 19,
        "subject": "Science"
    }
}

print(nested_student["Eshan"]["location"])  # Output: Rajshahi
print(nested_student["Arya"]["subject"])   # Output: Science

