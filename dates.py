import datetime
a = datetime.datetime.now()
print(a.strftime("%a"))

#Output: Mon

#%a gives the abbreviated weekday name (e.g., Sun, Mon).

import datetime
a = datetime.datetime.now()
print(a.strftime("%A"))

#Output:Monday

#%A gives the full weekday name (e.g., Sunday, Monday).


import datetime
a = datetime.datetime.now()
print(a.strftime("%D"))

#Output: 12/02/24

#%D gives the date in the format MM/DD/YY.


import datetime
a = datetime.datetime.now()
print(a.strftime("%m"))  # Corrected syntax

#Output: 12

#%m gives the month as a zero-padded decimal number (e.g., 01 for January, 12 for December).

#To specifically know about the current month:
#If you want the name of the month instead of the number, you can use %B:

print(a.strftime("%B"))

#Output: December
