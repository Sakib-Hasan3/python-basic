#dictionaries in python
studentInfo = {
    "Eshan": "cse"
}

# Access and print the value for the key "Eshan"
print(studentInfo["Eshan"])



studentInfo = {
    "Eshan": {
        "location": "rajshahi",
        "study": "12",
        "subject": "commerce",
        "roll": 10,
        "number": 123541235
    }
}

# Print the entire dictionary
print(studentInfo)

# Access and print specific details
print("Location:", studentInfo["Eshan"]["location"])
print("Study Level:", studentInfo["Eshan"]["study"])
print("Subject:", studentInfo["Eshan"]["subject"])
print("Roll Number:", studentInfo["Eshan"]["roll"])
print("Contact Number:", studentInfo["Eshan"]["number"])
