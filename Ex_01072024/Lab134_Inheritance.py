# Inheritance
# Acquire the attribute and Behavior
# Data member and Methods

# concept in OOp
# that allows a class(child class) to inherit the attributes and methods of another class.(parent class)

# Types of Inheritance
# 1. Single Inheritance - 80% of the time
# 2. Multiple Inheritance - 20% of the time
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance là một dạng của Single Inheritance
# 5. Hybrid Inheritance là một dạng của Multiple Inheritance


# Single Inheritance là một dạng của Inheritance trong đó một class (gọi là child class) kế thừa từ một class khác (gọi là parent class).
# Điều này có nghĩa là child class sẽ kế thừa tất cả các thuộc tính và phương thức của parent class, 
# và có thể mở rộng hoặc ghi đè chúng nếu cần thiết.
class Grandparent: # Parent class, Base class, Super class
    key = "abc@123"
    def grandparent_method(self):
        return "Grandparent's method"

class Father(Grandparent):# Inheritance from Grandparent (child class)
    def parent_method(self):
        return "Parent's method"
    
parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)