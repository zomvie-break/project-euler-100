#!/usr/bin/env python3

def sum_digits(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result

print(sum_digits(2**1000))
