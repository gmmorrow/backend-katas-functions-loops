#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Gabrielle"


def add(x, y):
    """Add two integers."""

    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    result = 0
    for _ in range(abs(y)):
        result = add(result, x)
    return -result if y < 0 else result


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    result = 1
    for _ in range(n):
        result = multiply(result, x)
    return result


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    result = 1
    for i in range(1, x + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, add(a, b)
    return a


if __name__ == '__main__':
    # your code to call functions above
    pass
