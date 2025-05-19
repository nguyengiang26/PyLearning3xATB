# Multiple Inheritance
# # # 1 Parent - 1 Parent - 1 Child

class Father:
    def father_money(self):
        return "5"
    
    def home(self):
        return "This is from Father class"

class Mother:
    def mother_money(self):
        return "10"
    
    def home(self):
        return "This is from Mother class"

class Promod(Father, Mother):
    pass
    # def home(self):
    #     return "This is from Promod class"

son = Promod()
print(son.father_money())
print(son.mother_money())
print(son.home()) # # This is from Father class because Father class is inherited first in the child class.
# Method Resolution Order (MRO) - Python sẽ tìm kiếm phương thức trong các lớp cha theo thứ tự mà chúng được kế thừa.
# Nếu phương thức không được tìm thấy trong lớp con, Python sẽ tìm kiếm trong lớp cha đầu tiên, 
# sau đó là lớp cha thứ hai, và cứ tiếp tục như vậy cho đến khi nó tìm thấy phương thức hoặc không còn lớp nào để tìm kiếm.
# theo thứ tự từ trái sang phải

