# Demonstrating error handling in Python using try-except blocks

# Taking input from the user
inp = input("Enter the number: ")  

# Using try-except to handle errors
try:
    # Attempting to convert the input into an integer
    num = int(inp)  
    # If successful, this block will run, and we print "Valid Number!"
    print("Valid Number!")  
except:
    # If there is an error (e.g., input is not a valid number), this block will run
    print("Invalid Number!")  
