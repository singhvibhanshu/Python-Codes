# Demonstrating how to read a file and process its lines in Python

# Opening a file in read mode
reading_a_file = open("read_file.txt", 'r')  
# The open() function opens the file "read_file.txt" in read ('r') mode.

# Reading all lines from the file
f = reading_a_file.readlines()  
# The .readlines() method reads the entire file and returns a list of lines, including newline characters.

# Initializing an empty list to store processed items
list_items = []

# Looping through each line in the file
for items in f:  
    # Checking if the last character in the line is a newline ('\n')
    if items[-1] == '\n':
        # Removing the newline character from the end of the string using slicing
        list_items.append(items[:-1])  # Slicing removes the last character (the newline)
    else:
        list_items.append(items)  # If there’s no newline, append the line as it is.

# Printing the processed list of items
print(list_items)  
# Outputs the list of lines without trailing newline characters.

# Closing the file after reading
reading_a_file.close()  
# It's important to close the file to free up system resources.
