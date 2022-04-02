#!/usr/bin/env python3

def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = 2000000
result = 0
for i in range(2, n + 1):
    if check_prime(i):
        result += i
        # print(f'i: {i}\tresult: {result}')

print(result)                   # 142913828922
