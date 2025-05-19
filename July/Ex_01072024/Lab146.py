class MathUtils:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c=0):
        # This method overrides the previous one
        return a + b + c
    
math = MathUtils()
print(math.add(2, 3)) # Output: 5
print(math.add(2, 3, 4)) # Output: 9
# # # Phương thức add mới có ba tham số, trong đó tham số c là tùy chọn với giá trị mặc định là 0.
# # # Khi gọi phương thức add với hai tham số, nó sẽ trả về tổng của hai tham số.
# # # Khi gọi phương thức add với ba tham số, nó sẽ trả về tổng của ba tham số.
# # # Điều này cho phép bạn sử dụng cùng một tên phương thức với các tham số khác nhau trong lớp con mà không cần phải thay đổi tên phương thức trong lớp cha.