class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None


    # Behavior
    def walk(self):
        print("I can talk")

    def talk(self):
        print("I can walk")

    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")

# Create an object of the Person class
pradmod = Person()
pradmod.name = "Pradmod"
pradmod.id = 1234
pradmod.sleep()

surya = Person()
surya.name = "Surya"
surya.id = 1235