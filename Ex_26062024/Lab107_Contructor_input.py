# Constructor in Python
# take input and create a class


class Student:
    def __init__(self):
        self.name = input("Enter your name: ") # Taking input from user
        # self.name = "John Doe" # Default value
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"Name is: {self.name}, Age: {self.age}")
    
student = Student()