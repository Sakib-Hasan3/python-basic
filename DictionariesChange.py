#change item in dictionaries 

x= {
    "name" : "John",
    "age" : 30,
    "city" : "New york"
    
}

print(x["city"])
x.update({"city":"london"})
print("The updated dictionary is : ",x["city"])