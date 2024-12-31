inp = input("Enter the number: ")
try:
    num = int(inp)
    print("Valid Number!")
except ValueError:
    print("Invalid Number! Please enter a valid integer.")
