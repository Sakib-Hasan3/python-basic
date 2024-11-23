#exercise in set item

x = {"apple", "mango", "banana"}

if "apple" in x:
    print("Yes, apple is in the set")
else:
    print("No, apple is not in the set")

#remove an item in the list 

x.remove("apple")
print(x)

#add an item in the list

x.add("orange")
print(x)

#update the set list

y={1,2,3,4,5}
x.update(y)
print(x)