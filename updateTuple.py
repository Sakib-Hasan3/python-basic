ThisTuple = ("eshan", "ahad", "tutul", "hablu")
print(type(ThisTuple))  # Output: <class 'tuple'>

a = list(ThisTuple)     # Convert tuple to list
a[1] = "shahin"         # Update second element
a.append("Shakil")      # Append "Shakil" to the list
print(a)                # Output: ['eshan', 'shahin', 'tutul', 'hablu', 'Shakil']

b = tuple(a)            # Convert the list back to a tuple
print(b)                 # Output: ('eshan', 'shahin', 'tutul', 'hablu', 'Shakil')
