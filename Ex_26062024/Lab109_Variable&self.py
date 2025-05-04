# Variables in class
#   Loại biến	    Cách khai báo	Ý nghĩa                                                 Cách truy cập bên trong class	    Cách truy cập bên ngoài
#   Biến instance	self.name	    Biến gắn với từng object (mỗi object có bản riêng)      self.name	                        object.name
#   Biến class	    ClassName.name	Biến dùng chung cho mọi object                          ClassName.name	hoặc self.name      ClassName.name hoặc object.name
#   Biến cục bộ	    name	        Chỉ tồn tại trong hàm, không lưu trong object           name	                            Không thể truy cập bên ngoài hàm
# 
#  
# Self là gì?	Chính là object đang làm việc với
# Dùng ở đâu?	Trong tất cả các method thuộc lớp
# Có thể đổi tên self không?	Có, nhưng không nên (theo chuẩn Python)
# 
class Person:
    # Class variable
    species = "Human"

    # Instance variables
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def say_hi(self):
        greeting = "Hello" # Local variable
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
        # Acessing class variable inside instance method
        print(f"I am a {self.species}.") # self.name
        print(f"Species: {Person.species}") # Class.name

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Accessing class variable outside the class
print(Person.species)  # Class.name
print(p1.species)      # Instance.name


print(p1.name)        # Accessing instance variable    
print(Person.say_hi()) # Accessing instance method