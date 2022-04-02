#!/usr/bin/env python3

result = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        result += i
print(result)
