# super() method in inheritance
# The super() function in Python is used to call a method from a parent class. 
# It allows you to access inherited methods that have been overridden in a child class.


class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        super().home()  # Call the home method of Father class
        print("2BHK")

pramod = Son()
pramod.home() # 2BHK
