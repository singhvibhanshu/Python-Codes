# Conditional Statements in Python
# Conditional statements are used to execute specific code blocks based on given conditions.

# Asking the user to input their age
age = input("Enter your age: ")  
# The input() function captures user input as a string.

# Checking and handling age input with conditions
if 0 < int(age) < 18:  
    # The condition checks if the user's age is greater than 0 and less than 18.
    print("You can't vote.")  # This block executes if the condition is True.
elif int(age) >= 18:  
    # This block executes if the user's age is 18 or more.
    print("You can vote.")
else:
    # This block handles invalid age inputs (e.g., negative values or zero).
    print("Invalid Input.")
