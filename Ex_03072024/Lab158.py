class MyCustomeException(Exception):
    def __init__(self, *message):
        self.message = message
        super().__init__(message)

balance = 10000
withdraw = int(input("Enter amount to withdraw: "))
if withdraw > balance:
    raise Exception("Insufficient Balance")
else:
    print("Transaction Successful")
    print("Remaining Balance: ", balance-withdraw)


               