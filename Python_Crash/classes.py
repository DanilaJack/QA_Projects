# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


#Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and My balance is {self.balance}'

#Init user object
brad = User('Brad Travasy', 'Brad@gmail.com', 37)

#Init a customer object
Janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)
Janet.set_balance(500)
print(Janet.greeting())

brad.has_birthday()
print(brad.greeting())

print(type(brad))