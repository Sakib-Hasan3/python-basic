#loop dictionary in python

x ={
    "name": "John",
    "age": 30,
    "city" : "london"
}

for i in x:
    print(x[i])

#another way
    
for i in x.values() :
    print(i)


#another way

for i,j in x.items():
    print(i,j)
    
    