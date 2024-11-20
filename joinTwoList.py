#join two list in python
#two list is added by using + operator or extend() function
list1=[1,2,3]
list2=["a","b","c"]

list3=list1 + list2
print(list3)

# OR using extend()

x=[1,2,3,4]
y=[5,6,7,8]
x.extend(y)
print(x)  # Note that this modifies x

