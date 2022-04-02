#!/usr/bin/env python3

def sum_the_squares(n):
    result = 0
    for i in range(1,n+1):
        result += i**2
    return result

def square_the_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result ** 2

result = square_the_sum(100) - sum_the_squares(100)
print(result)
