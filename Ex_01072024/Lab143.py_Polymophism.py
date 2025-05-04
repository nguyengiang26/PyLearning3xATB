# Polymorphism 
# là một khái niệm trong lập trình hướng đối tượng cho phép các đối tượng khác nhau được xử lý theo cách giống nhau,

class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

Shape1 = Rectangle(5, 10)
print(Shape1.area()) # Output: 50

shape2 = Circle(7)
print(shape2.area()) # Output: 153.86
# Polymorphism cho phép bạn sử dụng cùng một tên phương thức trong các lớp khác nhau 
# mà không cần phải thay đổi tên phương thức trong từng lớp.