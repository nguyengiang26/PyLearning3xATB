# Method overriding - Phương thức trong lớp con có thể ghi đè phương thức trong lớp cha.
# # Điều này có nghĩa là nếu lớp con định nghĩa một phương thức với cùng tên và tham số như trong lớp cha,
# # thì phương thức trong lớp con sẽ được gọi thay vì phương thức trong lớp cha.

class MathUtils:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b):
        return a + b + 1
    
math = MathUtils()
print(math.add(2, 3)) # Output: 6
# # Phương thức add trong lớp MathUtils đã được ghi đè bởi phương thức add mới,
