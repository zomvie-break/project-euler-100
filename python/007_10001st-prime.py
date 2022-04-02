#!/usr/bin/env python3

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
i = 2
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
        print(f'{i} is a prime number! len of primes[]: {len(primes)}' )
    i += 1

print(f'The 10,001st prime number is: {primes[-1]}')
