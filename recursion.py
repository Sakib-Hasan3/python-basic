#recursion in python

def refun():
    print("sakin")
    refun()
    
refun( )

#another example 

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
