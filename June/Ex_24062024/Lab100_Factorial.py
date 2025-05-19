# Recursion là gì?
# Recursion là một phương pháp lập trình trong đó một hàm gọi lại chính nó để giải quyết một bài toán. 
# Phương pháp này thường được sử dụng để giải quyết các bài toán có cấu trúc lặp lại hoặc phân chia thành các phần nhỏ hơn.
# Recursion có thể giúp đơn giản hóa mã nguồn và làm cho nó dễ đọc hơn, nhưng cũng cần phải cẩn thận để tránh vòng lặp vô hạn.
# Để sử dụng recursion, bạn cần xác định điều kiện dừng (base case) để ngăn chặn việc gọi lại vô hạn.
# Điều kiện dừng là một điều kiện mà khi đạt được, hàm sẽ không gọi lại chính nó nữa và sẽ trả về một giá trị cụ thể.
# Ví dụ về recursion là tính giai thừa của một số nguyên dương n, được định nghĩa như sau:
# n! = n * (n-1)! với điều kiện dừng là 0! = 1.
#
# Key concepts of recursion:
# 1. Base case: The condition under which the recursion stops.
# 2. Recursive case: The part of the function that calls itself with a modified argument.

# Fractorial
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n*factorial(n - 1)
    
    
