import re

txt = "the rain in spain"

# Find all lowercase characters alphabetically between "a" and "m"
x = re.findall("[a-m]", txt) 
print(x)


import re
txt = "the rain in spain"

# Find all lowercase characters alphabetically between "a" and "m"
x = re.findall("rain", txt)

if x:
    print("Yes,the string starts with 'hello'")
    
else:
     print("no match")
