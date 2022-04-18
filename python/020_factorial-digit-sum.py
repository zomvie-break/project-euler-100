#!/usr/bin/env python3

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial( n - 1 )

def run(n):
    """
    returns the sum of the digits of n factorial.
    """
    n = factorial(100)

    result = 0
    for x in str(n):
        result += int(x)

    return result

if __name__ == '__main__':
    print(run(100))
