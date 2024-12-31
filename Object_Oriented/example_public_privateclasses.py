# Importing the module 'public_privateclasses' and the 'NotPrivate' class from it
import public_privateclasses  
from public_privateclasses import NotPrivate  

# Creating an instance of the 'NotPrivate' class and passing "Vibhanshu" as a parameter to the constructor
test = NotPrivate("Vibhanshu")  

# Calling the 'display()' method (public method) on the 'test' object
test.display()  

# Calling the '_display()' method (intended to be private) on the 'test' object
test._display()  
