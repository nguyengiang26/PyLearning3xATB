# Constructor in Python
#   A constructor is a special method that is called when an object is created. It initializes the object's properties/attributes.
#   In Python, the constructor is defined using the __init__() method.

class Dog:
    # Constructor
    def __init__(self, id, name, fur_color, breed):
        self.id = id
        self.name = name
        self.fur_color = fur_color
        self.breed = breed   

    def sleep(self):
        print("I can sleep")


dog1 = Dog("1", "Doffy", "Brown", "Labrador")
dog2 = Dog("2", "Tommy", "Black", "Poodle")

print(f'{dog1.name} is a {dog1.fur_color} {dog1.breed} dog.')
print(f'{dog2.name} is a {dog2.fur_color} {dog2.breed} dog.')