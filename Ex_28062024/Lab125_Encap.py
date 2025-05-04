# Encapsulation là gì?
# Hide the data members (class variables/instance variables) of a class from outside access.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password = "456" # This can be accessed from inside the class
        print("Password changed to 456")


suv = Car()
suv.password = "345" # This can be accessed from outside the class
print(suv.password) # 345