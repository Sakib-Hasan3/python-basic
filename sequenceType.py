# sequence data type (list)
li = ['eshan', 'tutul', 'hasibul']
li[0] = 'hablu'  # changing the first element
print(type(li))  # This will print <class 'list'>

# tuple type data
tup = (5, 10, 15, 20, 25)
print(type(tup))  # This will print <class 'tuple'>

# range type data
ran = range(6)

# Using a loop to print elements in the range
for i in ran:
    print(i)  # This will print numbers from 0 to 5
