def factorial_recursive(n: int):
    if n == 0 or n == 1: # type: ignore
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))