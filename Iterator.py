list=[1,2,3,4,"x","y","z"]

print(list[0])

for i in list:
    print(i)
    
#The iter() method returns an iterator for the given argument.
#The next() function returns the next item from an iterator
    x=iter(list)
    print(next(x))
    
    