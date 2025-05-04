class Car:
    name = None

    def __init__(self):
        self.public = "Public"
        self.__private_var = "Private" # Private variable
        self._protected_var = "Protected" # Protected variable là gì?
        # Protected variable là biến mà chỉ có thể truy cập từ class cha và class con
        # Private variable là biến mà chỉ có thể truy cập từ class cha và class con

    def public_method(self):
        if self.__private_var == "123":
            print("Private variable is 123")
        else:
            print("This is a public method")
        

    def __private_method(self):
        print("This is a private method")

alto = Car()
print(alto.public_method()) # Public

print(alto.__private_method()) # Private - Error: 'Car' object has no attribute '__private_method'