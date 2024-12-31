# Demonstrating a while loop with a break condition

# Initializing the loop condition
loop = True  

# Starting a while loop that runs as long as 'loop' is True
while loop:  
    # Taking input from the user
    text = input("Write anything: ")  
    
    # Checking if the input is equal to the string "quit"
    if text == "quit":
        loop = False  # Setting loop to False to end the loop
        break  # Breaking out of the while loop immediately
