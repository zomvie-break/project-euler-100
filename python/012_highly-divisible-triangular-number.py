#!/usr/bin/env python3

def generate_triangular_number(n):
    '''
    returns triangular number of n
    '''
    return sum(range(n+1))

def find_divisors(n):
    '''
    returns all the factors of n
    '''
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            # print(f'n: {n}\ti: {i}\tn/i: {n/i}')
            result=list.__add__(result, [i, n/i])

    return list(set(result))


divisors = []
i = 2
# runs until it finds a triangular number with at least 500 factors.
while len(divisors) < 500:
    tri_numbers = generate_triangular_number(i)
    divisors = find_divisors(tri_numbers)
    # print(f'n: {tri_numbers}\t# of divisors: {len(divisors)}')
    i += 1

# print the triangular number with at least 500 factors
print(tri_numbers)
