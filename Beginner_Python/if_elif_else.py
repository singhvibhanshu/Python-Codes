# Conditional Statements in Python
# Conditional statements are used to execute code blocks based on specific conditions.

# Asking the user to input their age
age = input("Enter your age: ")  
# The input() function captures user input as a string.

# Converting the age input to an integer for comparison
if int(age) < 18:  
    # The condition checks if the user's age is less than 18.
    print("You can't vote.")  # This block executes if the condition is True.
else:
    # This block executes if the condition is False (age is 18 or more).
    print("You can vote.")
