# Web automation - Selenium
# Page - Your are going to automate


class VWLoginPage:
    email = None
    password = None

    def __init__(self):
        self.email = (input("Enter your email: "))
        self.password = input("Enter your password: ")

    def login_confirm(self):
        while self.password != "Pass123":
            print("Not allowed")
            self.__init__()
        print("Allowed")
        

amit = VWLoginPage()
amit.login_confirm()