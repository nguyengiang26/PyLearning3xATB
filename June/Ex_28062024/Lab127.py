class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100
    
    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print(f"Your balance is: {self.balance}")
        return self.balance

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")
    
    def if_you_are_auth_user(self, auth, amount1):
        if auth:
            self.__withdraw(amount=amount1)
        else:
            print("Not allowed")

jp_chase = BankAccount()
jp_chase.deposit(1000)


# secret_pass= input("Enter your PIN to show balance:")
# if secret_pass == "1234":
#     jp_chase.if_you_are_auth(True)
# else:
#     jp_chase.if_you_are_auth(False)


for i in range(6):
    secret_pass = input("Enter your PIN to withdraw: ")
    if secret_pass == "1234":
        your_amount = int(input("Enter your amount to withdraw: "))
        jp_chase.if_you_are_auth_user(True, amount1=your_amount)
        jp_chase.if_you_are_auth(True)
        break
    else:
        print("Incorrect PIN")
        if i>0:
            print("You have", 5-i, "attempts lefts")
        else:
            print("you exceeded the number of attempts")