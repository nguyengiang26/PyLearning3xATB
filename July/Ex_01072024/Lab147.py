# Abtraction là gì?
# # Abtraction là một trong những nguyên tắc cơ bản của lập trình hướng đối tượng (OOP) trong Python.
# # Nó cho phép bạn ẩn đi các chi tiết không cần thiết và chỉ hiển thị những thông tin quan trọng cho người dùng.
# # Điều này giúp giảm độ phức tạp và tăng tính dễ hiểu của mã nguồn.
# # Abtraction có thể được thực hiện thông qua các lớp trừu tượng (abstract classes) và các phương thức trừu tượng (abstract methods).

from abc import ABC, abstractmethod # from abc folder import ABC class, abdtractmethod method

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.sound()) # Output: Woof!