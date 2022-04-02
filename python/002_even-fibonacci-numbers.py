#!/usr/bin/env python3

result = 0
prev_term = 0
prev_prev_term = 0
current_term = 1

while current_term < 4*10**6:
    prev_prev_term = prev_term
    prev_term = current_term

    current_term = prev_prev_term + prev_term

    if current_term%2 == 0:
        result += current_term

print(result)
