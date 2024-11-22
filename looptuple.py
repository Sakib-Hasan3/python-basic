#loop in python 

x = ("hasan", "mahir", "karim", "mahi", "karim")

for i in x:
    print(i)


#another way of declaring loop tuple

x = ("dog", "cat", "mouse", "cow")

for i in range(len(x)):
    print(x[i])


#by using while loop

i = 0
while i < len(x):
    print(f"Index {i}: {x[i]}")
    i += 1
