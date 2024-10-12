# class Meta(type):
#     def __new__(self, class_name, bases, attrs):
#         print(attrs)
#         return type(class_name, bases, attrs)

# class Dog(metaclass = Meta):
#     x = 5
#     y = 8

# d = Dog()

class Meta(type):
    def __new__(self, class_name, bases, attrs):

        a = {}
        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, attrs)
    
class Dog(metaclass = Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
print(d.hello())