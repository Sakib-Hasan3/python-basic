#unpack tuples 

fruits=("apple","bannana","cherry")

(a,b,c)= fruits

print(b)
print(a)

fruits=("apple","bannana","cherry","Dog","egge","hablu","eshan")


(*a,) =fruits #using * to unpack the tuple into a list
print(a)

(a,*b) =fruits
print(b) #print from index b

(a,b,*c)=fruits
print(c) #print from index c

(a,b,*f,c)=fruits
print(f)