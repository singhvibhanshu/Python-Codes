# metaclasses are extremely complex thing.
# here, we'll only see an overview of it.

# the basic idea is that a class defines the rules for an object
# metaclass -> defines the rule for a class

class Test():
    pass

print(type(Test))

# now, this is something which we called as metaclasses