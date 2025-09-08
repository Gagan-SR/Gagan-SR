def factorial_recursive(n):
    """
    This function calculates the factorial of a non-negative integer using recursion.
    """
    # Base case: if n is 0 or 1, the factorial is 1.
    if n == 0 or n == 1:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")
