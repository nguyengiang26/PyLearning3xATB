# LeetCode - Sum of Digits
# Problem: Given an integer n, return the sum of its digits until we get a single digit.
# Example: Input: n = 38, Output: 2 (3 + 8 = 11, 1 + 1 = 2)
#
# Approach: We can use recursion to solve this problem. 
# The base case is when n is less than 10, in which case we return n. 
# Otherwise, we can sum the digits of n and call the function recursively with the sum until we get a single digit.

def sum_of_digits(n):
    # Base case: if n is less than 10, return n
    if n < 10:
        return n
    else: # Recursive case: sum the digits of n
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return sum_of_digits(digit_sum)
    
print(sum_of_digits(10)) # Output: 2