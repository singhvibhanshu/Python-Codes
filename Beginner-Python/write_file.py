# Demonstrating how to write to a file in Python

# Opening a file in write mode ('w')
writing_a_file = open("write_file.txt", 'w')  
# The 'w' mode opens the file for writing. If the file already exists, it will overwrite its content.

# Writing a string to the file
writing_a_file.write("Hello! I am learning Python.")  
# The write() method writes the specified string to the file.

# Closing the file after writing
writing_a_file.close()  
# It's important to close the file after writing to ensure data is saved properly and resources are released.
