# Demonstrating string methods: .strip(), len(), .lower(), .upper(), .split()

# .strip() -> removes all the blank spaces from the front and end of the string
text1 = input("Write something with blank spaces: ")  
# The input() function takes a string input from the user.
print(text1.strip())  
# The .strip() method removes any leading and trailing whitespace (spaces, tabs, etc.) from the string.

# len() -> for finding the length of the string
text2 = input("Enter something to find its length: ")  
# Takes input from the user to find the length of the string.
print(len(text2))  
# The len() function returns the number of characters in the string, including spaces.

# .split() -> separates each word and puts them in a list
text3 = input("Type something: ")  
# Takes a string input from the user.
print(text3.split())  
# The .split() method by default splits the string at spaces and returns a list of words.
# If you pass an argument to .split(), it will split at that character (e.g., '.split('.')' splits at periods).

# Example with .split('.') which splits at periods
print(text3.split('.'))  
# This splits the input text at every period ('.') and returns a list of substrings.
