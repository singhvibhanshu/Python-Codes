# Demonstrating the use of .find() and .count() methods in Python strings

# Defining a string
text = "Hey there! I am Vibhanshu Singh. I live in Delhi."
# The string contains a mix of words, spaces, punctuation, and uppercase/lowercase letters.

# Using the .find() method
print(text.find('e'))  
# The .find() method returns the index of the first occurrence of the specified substring.
# In this case, it returns 1 because the first 'e' is at index 1 (0-based indexing).

# Using the .count() method
print(text.count('e'))  
# The .count() method returns the total number of occurrences of the specified substring.
# In this case, it counts all the 'e' characters in the string and returns 6.
