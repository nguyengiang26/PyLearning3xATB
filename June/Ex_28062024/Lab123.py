# Web automation - Selenium
# Page - Your are going to automate


class VWLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Allow to enter")
        else:
            print("Not allowed")

amit = VWLoginPage("pramod@gmail.com", "Pass123")
amit.login_confirm()