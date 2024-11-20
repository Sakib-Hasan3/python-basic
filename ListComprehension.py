#list comprehension in python

x=["apple","mango","bananna","cherry"]
newlist=[]
for i in x:
    if "a" in i:
        newlist.append(i)
        print(newlist)

#newlist = [expression for item in iterable if condition == True]

number=[1,2,3,4,5]
new=[]
for i  in number:
    new.append(2*i)
    print(new)
    
#using comprehesion

number = [4, 5,6,3, 4, 5]  # Example list
double = [i * 2 for i in number]  # Multiply each element by 2
print(double)
