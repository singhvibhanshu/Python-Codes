# Demonstrating string slicing in Python

# Defining a string
text = "Hey! I am Vibhanshu Singh."  

# Using string slicing to extract a portion of the string
print(text[0: 4])  
# Syntax: text[start:stop:step]
# 'start' is the index to start slicing (inclusive), 
# 'stop' is the index to stop slicing (exclusive), 
# and 'step' is an optional parameter to define how to increment the slicing.
# In this case, it slices from index 0 to 4 (exclusive), so it prints "Hey!".

# Breakdown:
# text[0: 4] extracts characters starting from index 0 up to (but not including) index 4.
# So, it will output "Hey!" (positions 0, 1, 2, 3).
