#for loop

x=["mahi","Sumaiya","bubli","porimoni"]

#for variable in list name
for prem in x :
    print(prem)
    
    
#use range() and len() functions to create a suitabke iterable

for i in range(len(x)) :
    print(i)
    
#Iterating Over a String

for char in "Python":
    print(char)
    
#nested for loop

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


#break and continue loop

for i in range(5):
    if i == 3:
        break  # Exit loop when i equals 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip this iteration
    print(i)


#else block in for loop

for i in range(5):
    print(i)
else:
    print("Loop is finished!")


#use while loop

x = ["apple", "banana", "cherry"]
y = 0

while y < len(x):
    print(x[y])
    y += 1  # Increment y to avoid an infinite loop